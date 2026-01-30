# 禅道 API Skill

这是一个用于与禅道项目管理系统（ZenTao PMS）进行交互的 Claude Code Skill，提供了完整的 Python 客户端和 RESTful API v1.0 文档。

## ⚠️ 版本兼容说明

**本 Skill 仅兼容禅道 RESTful API v1.0 版本。**

- 禅道 RESTful API v1 在禅道开源版 16.5 及之后版本可用
- API 入口文件位于【禅道项目目录/www/api.php/v1】
- 不兼容其他版本的 API（如 v2 或其他自定义接口）
- 使用前请确认您的禅道实例版本支持 v1 API

## 功能特性

- **完整的 API 封装**：涵盖产品、项目、任务、Bug、用例、文档等核心模块
- **Token 认证**：基于 Token 的身份验证机制
- **丰富的接口**：支持获取、创建、更新、删除各类资源
- **详细文档**：包含完整的 API 使用说明和最佳实践

## 环境要求

- Python 3.6+
- python-dotenv
- requests

## 安装

1. 克隆或下载本项目到本地

2. 安装依赖：
```bash
pip install python-dotenv requests beautifulsoup4
```

3. 配置环境变量：

复制 `.env.example` 为 `.env`：
```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的禅道实例信息：
```bash
ZENTAO_BASE_URL=https://your-zentao-instance.com/api.php/v1
ZENTAO_ACCOUNT=your-username
ZENTAO_PASSWORD=your-password
```

## 使用方法

### 方式一：作为 Claude Code Skill 使用

将此项目配置为 Claude Code 的 Skill 后，即可直接在对话中调用禅道 API：

```
请帮我获取所有产品列表
创建一个新的 Bug，标题是"登录页面异常"
```

### 方式二：直接使用 Python 客户端

```python
import sys
import os

# 将 scripts 目录添加到路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from zentao_client import get_client

# 初始化客户端（会自动从 .env 文件读取配置）
client = get_client()

# 1. 获取产品列表
products = client.get_products()
print(f"找到 {len(products)} 个产品")

if products:
    product_id = products[0]['id']

    # 2. 获取产品的 Bug 列表
    result = client.get_product_bugs(product_id)
    bugs = result.get('bugs', [])
    print(f"产品有 {len(bugs)} 个 Bug")

    # 3. 获取测试用例
    cases = client.get_product_cases(product_id)
    print(f"产品有 {len(cases)} 个测试用例")

    # 4. 创建计划
    client.create_plan(product_id, {
        "title": "新版本发布计划",
        "begin": "2024-01-01",
        "end": "2024-12-31"
    })
```

## 常见用法示例

### 获取项目列表

```python
client = get_client()
result = client.get_projects()
projects = result.get('projects', [])
total = result.get('total', 0)

print(f"共有 {total} 个项目")
for project in projects:
    print(f"  - {project.get('name')} (ID: {project.get('id')})")
```

### 获取某个项目的所有 Bug（处理分页）

```python
import requests

client = get_client()
project_id = 22

all_bugs = []
page = 1
limit = 100

while True:
    url = f"{client.base_url}/projects/{project_id}/bugs"
    params = {'page': page, 'limit': limit}
    response = requests.get(url, headers=client.headers, params=params)
    data = response.json()

    bugs = data.get('bugs', [])
    all_bugs.extend(bugs)

    total = data.get('total', 0)
    if len(all_bugs) >= total:
        break
    page += 1

print(f"项目共有 {len(all_bugs)} 个 Bug")
```

### 创建一个 Bug

```python
client = get_client()
product_id = 1

bug_data = {
    "title": "登录页面无法正常显示",
    "openedBuild": "trunk",
    "severity": "3",
    "pri": "2",
    "type": "bug"
}

bug = client.create_bug(product_id, bug_data)
print(f"Bug 创建成功，ID: {bug.get('id')}")
```

## 支持的 API 模块

| 模块 | 说明 |
|------|------|
| **认证** | Token 获取和验证 |
| **用户** | 用户管理、个人信息 |
| **部门** | 部门列表和详情 |
| **产品** | 产品管理 |
| **项目** | 项目管理 |
| **执行** | 执行/冲刺管理 |
| **任务** | 任务管理 |
| **Bug** | Bug 管理和跟踪 |
| **需求** | 需求（Story）管理 |
| **计划** | 产品计划管理 |
| **发布** | 版本发布管理 |
| **测试** | 测试用例、测试套件 |
| **文档** | 文档库管理 |
| **反馈** | 用户反馈管理 |
| **工单** | 工单管理 |

## 重要提示

### 1. API 返回结构

大部分列表接口返回的是**分页字典**，而非直接返回列表：

```python
# 错误用法
projects = client.get_projects()
for p in projects:  # TypeError: projects 是字典，不是列表！
    print(p['name'])

# 正确用法
result = client.get_projects()
# result = {"page": 1, "total": 10, "limit": 20, "projects": [...]}
projects = result.get('projects', [])
total = result.get('total', 0)
```

### 2. 分页处理

API 默认每页返回 20 条数据。对于大数据集，需要手动处理分页：

```python
# 一次只获取 20 条（不完整）
result = client.get_product_bugs(product_id)
bugs = result.get('bugs', [])  # 可能只有 20 条，但实际有 722 条

# 需要循环获取所有页
all_bugs = []
page = 1
while True:
    url = f"{client.base_url}/products/{product_id}/bugs"
    params = {'page': page, 'limit': 100}
    response = requests.get(url, headers=client.headers, params=params)
    data = response.json()
    bugs = data.get('bugs', [])
    all_bugs.extend(bugs)
    if len(all_bugs) >= data.get('total', 0):
        break
    page += 1
```

### 3. 项目与产品的关系

禅道中项目和产品是独立的，项目可能没有关联产品（`hasProduct: 0`）。

对于没有产品的项目，Bug 和需求需要通过项目端点直接获取：

```python
# 获取项目的 Bug（不通过产品）
url = f"{client.base_url}/projects/{project_id}/bugs"
response = requests.get(url, headers=client.headers)
bugs = response.json().get('bugs', [])
```

### 4. 调试未知响应结构

遇到意外错误时，先检查响应结构：

```python
import json

result = client.some_method()

# 1. 检查类型
print(f"类型: {type(result)}")

# 2. 如果是字典，打印所有键
if isinstance(result, dict):
    print(f"键: {list(result.keys())}")

# 3. 打印完整响应（截断大内容）
print(json.dumps(result, indent=2, ensure_ascii=False)[:2000])
```

## 文档目录

完整的 API 文档位于 `resources/api_v1/` 目录：

- [Guide](resources/api_v1/Guide.md) - 配置使用与常见问题
- [Authentication](resources/api_v1/Authentication.md) - 认证接口
- [Products](resources/api_v1/Products.md) - 产品接口
- [Projects](resources/api_v1/Projects.md) - 项目接口
- [Bugs](resources/api_v1/Bugs.md) - Bug 接口
- [Tasks](resources/api_v1/Tasks.md) - 任务接口
- [Stories](resources/api_v1/Stories.md) - 需求接口
- [QA](resources/api_v1/QA.md) - 测试接口
- 更多...

## 更新文档

如果禅道 API 有更新，可以重新抓取最新文档：

```bash
cd scripts
python scrape_docs.py  # 抓取最新文档
python split_docs.py   # 拆分到各模块
```

## 许可证

本项目文档来源于禅道官方 API 文档。

## 相关链接

- [禅道官网](https://www.zentao.net/)
- [禅道 API 文档](https://www.zentao.net/book/api/zentaoapi1397.html)
