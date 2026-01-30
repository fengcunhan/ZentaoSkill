# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ZentaoSkill provides a Python client and documentation for interacting with the 禅道 (ZenTao) Project Management System via RESTful API v1.0. ZenTao is an integrated project management platform supporting products, projects, QA, bug tracking, and documentation.

## Architecture

### Python Client (`scripts/zentao_client.py`)

The `ZentaoClient` class provides a Pythonic interface to the ZenTao API. Key architectural patterns:

- **Authentication**: Token-based via `/tokens` endpoint, stored in `self.headers['Token']`
- **HTTP Methods**: Private `_get()`, `_post()`, `_put()`, `_delete()` wrappers that handle `requests` calls
- **Environment Loading**: Uses `python-dotenv` to load credentials from `.env` file at project root

### API Response Structures

**Critical**: Most list endpoints return paginated dictionaries, not direct lists:

```python
# WRONG: Assumes list returned
projects = client.get_projects()
for p in projects:  # TypeError - projects is a dict!

# CORRECT: Access nested data
result = client.get_projects()
# result = {"page": 1, "total": 10, "limit": 20, "projects": [...]}
projects = result.get('projects', [])
```

**Pagination Handling**: Default limit is 20 items per page. For large datasets, manually paginate:

```python
url = f"{client.base_url}/projects/{id}/bugs"
all_bugs = []
page = 1
limit = 100

while True:
    params = {'page': page, 'limit': limit}
    response = requests.get(url, headers=client.headers, params=params)
    data = response.json()
    bugs = data.get('bugs', [])
    all_bugs.extend(bugs)
    if len(all_bugs) >= data.get('total', 0):
        break
    page += 1
```

### Project vs Product Relationships

ZenTao has a hierarchical structure that can be confusing:

- **Programs** (项目集) - Top-level project collections
- **Projects** (项目) - Development projects
- **Products** (产品) - Products being developed
- **Executions** (执行) - Sprints/builds within projects

**Gotcha**: Projects may have `hasProduct: 0`, meaning no product linkage. In such cases, bugs and stories exist directly under the project, not via a product.

### Documentation Generation Pipeline

`scripts/` contains utilities for generating/splitting documentation:

1. **`scrape_docs.py`** - Scrapes ZenTao's official API documentation from zentao.net
   - Reads `api_list.json` for URLs to scrape
   - Parses HTML tables into Markdown format
   - Outputs to `resources/ZenTao_API_v1.0.md`

2. **`split_docs.py`** - Splits comprehensive docs into categorized modules
   - Reads `resources/ZenTao_API_v1.0.md`
   - Classifies sections by regex rules (Auth, Products, Projects, Bugs, etc.)
   - Writes separate files to `resources/api_v1/`

## Environment Setup

Copy `.env.example` to `.env` and configure:

```bash
ZENTAO_BASE_URL=https://your-zentao-instance.com/api.php/v1
ZENTAO_ACCOUNT=your-username
ZENTAO_PASSWORD=your-password
```

## Dependencies

```bash
pip install python-dotenv requests beautifulsoup4
```

## Common Development Tasks

### Using the Client

```python
import sys
sys.path.append('scripts')
from zentao_client import get_client

client = get_client()  # Loads from .env automatically

# Get products
products = client.get_products()

# Get project bugs (with pagination awareness)
import requests
url = f"{client.base_url}/projects/22/bugs"
response = requests.get(url, headers=client.headers, params={'limit': 100})
bugs = response.json().get('bugs', [])
```

### Re-generating Documentation

If the ZenTao API is updated:

```bash
cd scripts
python scrape_docs.py  # Scrape latest docs
python split_docs.py   # Re-split into modules
```

### Adding New API Methods

When adding endpoints to `ZentaoClient`:

1. Check if the endpoint returns a list or paginated dict
2. For paginated responses, document the structure in the docstring
3. Use the private HTTP wrappers (`_get`, `_post`, etc.)
4. Follow existing naming: `get_{entity}`, `create_{entity}`, `update_{entity}`, `delete_{entity}`

## Known Pitfalls

1. **Assuming direct list returns** - Always check response structure with `type(response)` and `response.keys()`
2. **Project without product** - Use direct project endpoints (e.g., `/projects/{id}/bugs`) instead of product endpoints when `hasProduct: 0`
3. **Pagination limits** - Default 20 items; manual pagination required for full datasets
4. **Multipart file uploads** - The `upload_file()` method handles special headers for file uploads
