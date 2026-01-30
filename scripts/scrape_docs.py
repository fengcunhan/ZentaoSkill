import json
import os
import time
import requests
from bs4 import BeautifulSoup

def fetch_docs():
    json_path = os.path.join(os.path.dirname(__file__), 'api_list.json')
    output_path = os.path.join(os.path.dirname(__file__), '../resources/ZenTao_API_v1.0.md')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        api_list = json.load(f)
    
    # Initialize output file with header
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# ZenTao RESTful API v1.0 Comprehensive Documentation\n\n")
        f.write("> Generated from official documentation.\n\n")

    print(f"Starting scrape of {len(api_list)} pages...")
    
    for i, item in enumerate(api_list):
        url = item['url']
        title = item['title']
        
        print(f"[{i+1}/{len(api_list)}] Fetching {title}: {url}")
        
        try:
            # Add a small delay to be polite
            time.sleep(0.2)
            
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            
            soup = BeautifulSoup(resp.content, 'html.parser')
            
            article = soup.find(class_='article-content')
            
            content = ""
            if article:
                # Helper to convert table to markdown
                for table in article.find_all('table'):
                    markdown_table = []
                    # Get headers
                    # Find the first row that looks like a header (contains th) or just first row
                    rows = table.find_all('tr', recursive=False)
                    # If empty, maybe tbody exists
                    if not rows:
                        tbody = table.find('tbody', recursive=False)
                        if tbody:
                            rows = tbody.find_all('tr', recursive=False)
                    
                    if not rows:
                        continue

                    headers = []
                    header_row = rows[0]
                    # Malformed HTML has nested cells (tr -> th -> th -> th).
                    # recursive=False only finds the first one.
                    # We MUST search recursively to find all of them.
                    # Our text extraction logic (only direct strings) prevents duplicating content.
                    
                    all_cells_in_row = header_row.find_all(['th', 'td']) # Recursive by default
                    
                    for cell in all_cells_in_row:
                        # CRITICAL FIX: Only include cells that belong to THIS row.
                        # Because of weird nesting (tr inside td inside tr), searching find_all on the outer tr
                        # returns cells from inner trs too.
                        # We check if the closest 'tr' ancestor is indeed the current row.
                        if cell.find_parent('tr') != header_row:
                            continue

                        # Extract only direct text content
                        text = "".join([str(c) for c in cell.contents if isinstance(c, str) or c.name == 'br']).strip()
                        text = text.replace('\n', ' ').strip()
                        if text:
                            headers.append(text)
                    
                    if not headers:
                        continue
                        
                    markdown_table.append("| " + " | ".join(headers) + " |")
                    markdown_table.append("| " + " | ".join(['---'] * len(headers)) + " |")
                    
                    # Get rows
                    for row in rows[1:]: # Skip header
                        cols = []
                        # Same logic for rows: recursive find, direct text extract, parent check
                        all_cells_in_row = row.find_all(['td', 'th'])
                        for cell in all_cells_in_row:
                            if cell.find_parent('tr') != row:
                                continue
                                
                            text = "".join([str(c) for c in cell.contents if isinstance(c, str) or c.name == 'br']).strip()
                            text = text.replace('\n', ' ').strip()
                            if text:
                                cols.append(text)
                        
                        # Pad columns if necessary to match header length
                        if len(cols) < len(headers):
                            cols.extend([''] * (len(headers) - len(cols)))
                        
                        # Only add if it somewhat matches
                        if any(cols):
                            markdown_table.append("| " + " | ".join(cols) + " |")
                    
                    # Replace table with markdown
                    new_div = soup.new_tag('div')
                    new_div.string = "\n" + "\n".join(markdown_table) + "\n"
                    table.replace_with(new_div)

                # Helper to format code blocks (often in div.code or pre)
                # ZenTao docs might use different classes, let's look for likely candidates
                for code_block in article.find_all(['pre', 'code']):
                    text = code_block.get_text(strip=True)
                    # Check if it looks like JSON
                    if text.startswith('{') or text.startswith('['):
                        new_code = soup.new_tag('div')
                        new_code.string = f"\n```json\n{text}\n```\n"
                        code_block.replace_with(new_code)
                
                # Convert Headers to Markdown Headers
                for i in range(1, 7):
                    for h in article.find_all(f'h{i}'):
                        h_text = h.get_text(strip=True)
                        h.replace_with(f"\n{'#' * (i+1)} {h_text}\n")

                content = article.get_text(separator='\n', strip=True)
                # Cleanup multiple newlines
                import re
                content = re.sub(r'\n{3,}', '\n\n', content)
            else:
                content = "Content extraction failed. Please visit URL."

            # Append to file
            with open(output_path, 'a', encoding='utf-8') as f:
                f.write(f"\n\n---\n\n## {i+1}. {title}\n")
                f.write(f"**Source**: {url}\n\n")
                f.write(content)
                f.write("\n")
                
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            with open(output_path, 'a', encoding='utf-8') as f:
                f.write(f"\n\n---\n\n## {i+1}. {title}\n")
                f.write(f"**Error fetching content**: {e}\n")

    print(f"Done. Saved to {output_path}")

if __name__ == "__main__":
    fetch_docs()
