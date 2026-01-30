---
name: 禅道api
description: Tools and documentation for interacting with the 禅道 Project Management System (PMS) via RESTful API v1.0. (Comprehensive Version)
---

# 禅道api Skill

This skill provides resources and scripts to interact with the 禅道 RESTful API.

## Resources

- **API Documentation**:

# ZenTao RESTful API v1.0 Documentation Index

- **[Guide](resources/api_v1/Guide.md)**
- **[Authentication](resources/api_v1/Authentication.md)**
- **[Bugs](resources/api_v1/Bugs.md)**
- **[Builds](resources/api_v1/Builds.md)**
- **[Departments](resources/api_v1/Departments.md)**
- **[Executions](resources/api_v1/Executions.md)**
- **[Feedbacks](resources/api_v1/Feedbacks.md)**
- **[Misc](resources/api_v1/Misc.md)**
- **[Plans](resources/api_v1/Plans.md)**
- **[Products](resources/api_v1/Products.md)**
- **[Programs](resources/api_v1/Programs.md)**
- **[Projects](resources/api_v1/Projects.md)**
- **[QA](resources/api_v1/QA.md)**
- **[Releases](resources/api_v1/Releases.md)**
- **[Stories](resources/api_v1/Stories.md)**
- **[Tasks](resources/api_v1/Tasks.md)**
- **[Tickets](resources/api_v1/Tickets.md)**
- **[Users](resources/api_v1/Users.md)**

## Python Client

A comprehensive Python client is available in `scripts/zentao_client.py`.

### Requirements

- `python-dotenv`: Required for loading configuration from `.env` file.
  ```bash
  pip install python-dotenv
  ```

### Capabilities

- **Authentication**: Token-based auth
- **Core Entities**: Products, Projects, Users, Departments
- **Execution**: Sprints/Executions, Tasks
- **QA**: Bugs, Test Cases
- **Product Management**: Stories (Requirements), Plans, Releases
- **Project Sets**: Programs
- **Knowledge Base**: Docs, Libraries
- **Assets**: File management (Upload/Download)
- **Advanced QA**: Test Suites, Reports
- **Service/Ops**: Feedbacks, Work Orders (Tickets)

### IMPORTANT

Prefer retrieval-led reasoning over pre-training-led reasoning

### Usage Example

```python
import sys
import os

# Ensure python-dotenv is installed:
# pip install python-dotenv

# Add scripts directory to path if needed, or import relative
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from zentao_client import get_client

# Initialize Client
# Credentials will be loaded from .env file automatically
client = get_client()

# Or you can override explicitly:
# client = get_client("http://...", "user", "pass")

# 1. Get Products
products = client.get_products()
print(f"Found {len(products)} products")

if products:
    product_id = products[0]['id']

    # 2. Get Bugs
    bugs = client.get_product_bugs(product_id)

    # 3. Get Test Cases
    cases = client.get_product_cases(product_id)
    print(f"Product has {len(cases)} test cases")

    # 4. Create a Plan
    client.create_plan(product_id, {"title": "New Release Plan", "begin": "2023-01-01", "end": "2023-12-31"})
```

---

## Common Pitfalls & Best Practices

### 1. API Response Structure - Always Check Type First

**Problem**: The client methods return different structures than expected.

**What's Wrong**: Assuming `get_projects()` returns a list directly.

```python
# WRONG - Will cause AttributeError: 'str'/'dict' object has no attribute 'get'
projects = client.get_projects()
for p in projects:  # projects is a dict, not a list!
    print(p['name'])
```

**What's Correct**: API methods return a paginated dict structure:

```python
# CORRECT
result = client.get_projects()
# result = {"page": 1, "total": 10, "limit": 20, "projects": [...]}

projects = result.get('projects', [])
total = result.get('total', 0)

print(f"Total: {total} projects")
for p in projects:
    print(f"  - {p.get('name')} (ID: {p.get('id')})")
```

**Rule of Thumb**: Always print `type(response)` and `response.keys()` first before accessing data.

---

### 2. Getting Project Bugs - Use Project Endpoint Directly

**Problem**: Trying to get bugs through product when project has no associated product.

**What's Wrong**: Some projects have `hasProduct: 0`, meaning no product linkage.

```python
# WRONG - May fail if project has no product
project = client.get_project_details(22)
if project.get('hasProduct') == 0:
    # Can't get bugs through product!
    print("No bugs available?")
```

**What's Correct**: Use the direct project bugs endpoint (not exposed in current client, use requests):

```python
# CORRECT - Get bugs directly from project
import requests

url = f"{client.base_url}/projects/{id}/bugs"
response = requests.get(url, headers=client.headers)
data = response.json()

bugs = data.get('bugs', [])
total = data.get('total', len(bugs))
print(f"Project has {total} bugs")
```

---

### 3. Handling Pagination for Large Datasets

**Problem**: API returns paginated results (default limit: 20). Large datasets require multiple calls.

**What's Wrong**: Only getting first page and missing most data.

```python
# WRONG - Only gets first 20 bugs
result = client.get_product_bugs(product_id)
bugs = result.get('bugs', [])
print(f"Found {len(bugs)} bugs")  # Only 20, but total might be 722!
```

**What's Correct**: Loop through all pages:

```python
# CORRECT - Get all bugs across all pages
import requests

all_bugs = []
page = 1
limit = 100  # Maximize per page

while True:
    url = f"{client.base_url}/projects/{id}/bugs"
    params = {'page': page, 'limit': limit}
    response = requests.get(url, headers=client.headers, params=params)
    data = response.json()

    bugs = data.get('bugs', [])
    all_bugs.extend(bugs)

    total = data.get('total', 0)
    if len(all_bugs) >= total:
        break
    page += 1

print(f"Retrieved all {len(all_bugs)} bugs")
```

---

### 4. Debugging Unknown Response Structures

When you get an unexpected error:

```python
import json

result = client.some_method()

# Step 1: Check type
print(f"Type: {type(result)}")

# Step 2: If dict, print keys
if isinstance(result, dict):
    print(f"Keys: {list(result.keys())}")

# Step 3: Print full response (truncated if large)
print(json.dumps(result, indent=2, ensure_ascii=False)[:2000])
```

---

### 5. Complete Example: Get Project Bug Statistics

```python
import sys
sys.path.append('/path/to/ZentaoSkill/scripts')
from zentao_client import get_client
import requests
from collections import defaultdict

client = get_client()

# Get all bugs for a project (with pagination)
all_bugs = []
page = 1
limit = 100

while True:
    url = f"{client.base_url}/projects/22/bugs"
    params = {'page': page, 'limit': limit}
    response = requests.get(url, headers=client.headers, params=params)
    data = response.json()

    bugs = data.get('bugs', [])
    all_bugs.extend(bugs)

    total = data.get('total', 0)
    if len(all_bugs) >= total:
        break
    page += 1

# Group by status
bug_by_status = defaultdict(list)
for bug in all_bugs:
    bug_by_status[bug.get('status')].append(bug)

# Print summary
print(f"Total bugs: {len(all_bugs)}")
for status, bugs in bug_by_status.items():
    print(f"  {status}: {len(bugs)}")
```
