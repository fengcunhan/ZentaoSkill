import os
import re
import shutil

SOURCE_FILE = '/Users/fch/Documents/github/ZentaoSkill/resources/ZenTao_API_v1.0.md'
OUTPUT_DIR = '/Users/fch/Documents/github/ZentaoSkill/resources/api_v1'

# Classification Rules (Tuple: Keyword/Regex, Category Name)
# Order matters! Specific matches first.
RULES = [
    (r'Token|Auth', 'Authentication'),
    (r'部门|Department', 'Departments'),
    (r'用户|User|个人信息', 'Users'),
    (r'项目集|Program', 'Programs'),
    (r'产品计划|Plan', 'Plans'),
    (r'产品发布|项目发布|Release', 'Releases'),
    (r'产品需求|项目需求|需求|Story', 'Stories'),
    (r'产品|Product', 'Products'),
    (r'项目|Project', 'Projects'),
    (r'执行|Execution', 'Executions'),
    (r'任务|Task', 'Tasks'),
    (r'Bug', 'Bugs'),
    (r'用例|TestCase|测试单|TestTask', 'QA'),
    (r'版本|Build', 'Builds'),
    (r'反馈|Feedback', 'Feedbacks'),
    (r'工单|Ticket', 'Tickets'),
    (r'文档|Doc|Lib', 'Docs'),
    (r'配置|Config|Usage|Common', 'Guide'),
]

def get_category(title, content):
    # Try to match title first
    for pattern, category in RULES:
        if re.search(pattern, title, re.IGNORECASE):
            return category
    
    # Fallback: check content for specific URL patterns if needed (e.g. /users)
    # But title should be sufficient for this specific doc file.
    return 'Misc'

def split_docs():
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: {SOURCE_FILE} not found.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Split by '---'
    # First part is header (usually)
    parts = re.split(r'\n---\n', full_content)
    
    header = parts[0]
    api_sections = parts[1:]
    
    # Organize by category
    categorized = {}
    
    for section in api_sections:
        lines = section.strip().split('\n')
        title = "Unknown"
        # Find the first H2 header
        for line in lines:
            if line.strip().startswith('## '):
                title = line.strip().replace('##', '').strip()
                break
        
        category = get_category(title, section)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(section)

    # Write Category Files
    generated_files = {}
    for category, sections in categorized.items():
        filename = f"{category}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        content = f"# ZenTao {category} API\n\n"
        content += "\n---\n".join(sections)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        generated_files[category] = filename
        print(f"Created {filename} with {len(sections)} sections.")

    # Rewrite Source File as Index
    index_content = "# ZenTao RESTful API v1.0 Documentation Index\n\n"
    index_content += "> This documentation is split into modules for easier navigation.\n\n"
    
    # Sort categories: Auth, Users, Products, Projects... (Guide first)
    sorted_cats = sorted(generated_files.keys())
    if 'Guide' in sorted_cats:
        sorted_cats.remove('Guide')
        sorted_cats.insert(0, 'Guide')
    if 'Authentication' in sorted_cats:
        sorted_cats.remove('Authentication')
        sorted_cats.insert(1, 'Authentication')

    for category in sorted_cats:
        filename = generated_files[category]
        index_content += f"- **[{category}](api_v1/{filename})**\n"
        
        # Optional: Add sub-links or summary? 
        # For now, just top level links as requested.

    with open(SOURCE_FILE, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("Index file created.")

if __name__ == "__main__":
    split_docs()
