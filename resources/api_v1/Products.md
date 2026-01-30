# ZenTao Products API


## 7. 获取产品列表

**Source**: https://www.zentao.net/book/api/675.html

#### 本篇目录

获取产品列表
请求URL
请求头
请求响应
响应示例
GET
/products

### 获取产品列表

#### 请求URL

https://xxx.com/api.php/v1/products

#### 请求头

| Token | String | 否  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| products | array | 是  |
| -------- | ----- | --- |

#### 响应示例

```json
{
  "total": 1,
  "products": [
    {
      "id": 6,
      "program": 6,
      "name": "测试",
      "code": "",
      "bind": "1",
      "line": 0,
      "type": "normal",
      "status": "normal",
      "subStatus": "",
      "desc": "",
      "PO": {
        "id": 2,
        "account": "productManager",
        "avatar": "",
        "realname": "产品经理"
      },
      "QD": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "RD": {
        "id": 2,
        "account": "productManager",
        "avatar": "",
        "realname": "产品经理"
      },
      "acl": "private",
      "whitelist": [
        {
          "id": 1,
          "account": "admin",
          "avatar": "",
          "realname": "管理员"
        },
        {
          "id": 2,
          "account": "productManager",
          "avatar": "",
          "realname": "产品经理"
        }
      ],
      "reviewer": "",
      "createdBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "createdDate": "2021-12-01T05:17:04Z",
      "createdVersion": "15.8",
      "order": 30,
      "deleted": "0",
      "lineName": "",
      "programName": "企业管理",
      "stories": {
        "0": "",
        "1": "draft",
        "2": "active",
        "3": "closed",
        "4": "changed",
        "": 0,
        "draft": 0,
        "active": 0,
        "closed": 0,
        "changed": 0
      },
      "requirements": {
        "0": "",
        "1": "draft",
        "2": "active",
        "3": "closed",
        "4": "changed",
        "": 0,
        "draft": 0,
        "active": 0,
        "closed": 0,
        "changed": 0
      },
      "plans": 0,
      "releases": 0,
      "bugs": 0,
      "unResolved": 0,
      "closedBugs": 0,
      "fixedBugs": 0,
      "thisWeekBugs": 0,
      "assignToNull": 0,
      "progress": 0
    }
  ]
}
```

---

## 7. 创建产品

**Source**: https://www.zentao.net/book/api/676.html

#### 本篇目录

创建产品
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/products

### 创建产品

#### 请求URL

https://xxx.com/api.php/v1/products

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 是  | 产品名称 |
| ---- | ------ | --- | -------- |

#### 请求示例

```json
{
  "name": "测试产品",
  "code": "test",
  "program": 1
}
```

#### 请求响应

| id  | int | 否  | 产品ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "total": 11,
  "products": [
    {
      "id": 1,
      "program": 6,
      "name": "公司企业网站建设1",
      "code": "companyWebsite",
      "bind": "0",
      "line": 0,
      "type": "normal",
      "status": "normal",
      "subStatus": "",
      "desc": "建立公司企业网站，可以更好对外展示。<br />",
      "PO": {
        "id": 2,
        "account": "productManager",
        "avatar": "",
        "realname": "产品经理"
      },
      "QD": {
        "id": 10,
        "account": "testManager",
        "avatar": "",
        "realname": "测试经理"
      },
      "RD": {
        "id": 2,
        "account": "productManager",
        "avatar": "",
        "realname": "产品经理"
      },
      "acl": "open",
      "whitelist": [],
      "reviewer": "",
      "createdBy": {
        "id": 2,
        "account": "productManager",
        "avatar": "",
        "realname": "产品经理"
      },
      "createdDate": "2012-06-05T01:57:07Z",
      "createdVersion": "",
      "order": 5,
      "deleted": "0",
      "lineName": "",
      "programName": "企业管理",
      "stories": {
        "active": 5,
        "draft": 3,
        "": 0,
        "closed": 0,
        "changed": 0
      },
      "requirements": {
        "0": "",
        "1": "draft",
        "2": "active",
        "3": "closed",
        "4": "changed",
        "": 0,
        "draft": 0,
        "active": 0,
        "closed": 0,
        "changed": 0
      },
      "plans": 0,
      "releases": 0,
      "bugs": 5,
      "unResolved": 5,
      "closedBugs": 0,
      "fixedBugs": 0,
      "thisWeekBugs": 1,
      "assignToNull": 1,
      "progress": 0
    }
  ]
}
```

---

## 7. 获取产品详情

**Source**: https://www.zentao.net/book/api/677.html

#### 本篇目录

获取产品详情
请求URL
请求头
请求响应
响应示例
GET
/products/id

### 获取产品详情

#### 请求URL

https://xxx.com/api.php/v1/products/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 产品ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "program": 6,
  "name": "公司企业网站建设1",
  "code": "companyWebsite",
  "bind": "0",
  "line": 0,
  "type": "normal",
  "status": "normal",
  "subStatus": "",
  "desc": "建立公司企业网站，可以更好对外展示。<br />",
  "PO": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "QD": {
    "id": 10,
    "account": "testManager",
    "avatar": "",
    "realname": "测试经理"
  },
  "RD": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "acl": "open",
  "whitelist": [],
  "reviewer": "",
  "createdBy": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "createdDate": "2012-06-05T01:57:07Z",
  "createdVersion": "",
  "order": 5,
  "deleted": "0",
  "stories": {
    "active": 5,
    "draft": 3,
    "": 0,
    "closed": 0,
    "changed": 0
  },
  "plans": 0,
  "releases": 0,
  "builds": 0,
  "cases": 5,
  "projects": 0,
  "executions": 0,
  "bugs": 5,
  "docs": 0,
  "progress": 0,
  "caseReview": false
}
```

---

## 7. 编辑产品

**Source**: https://www.zentao.net/book/api/678.html

#### 本篇目录

编辑产品
请求头
请求头
请求体
请求示例
请求响应
响应示例
PUT
/product/id

### 编辑产品

#### 请求头

https://xxx.com/api.php/v1/product/id

#### 请求头

| Token | String | 否  | 访问凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 否  | 产品名称 |
| ---- | ------ | --- | -------- |

#### 请求示例

```json
{
  "name": "公司企业网站建设1"
}
```

#### 请求响应

| id  | int | 是  | 产品ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "program": 6,
  "name": "公司企业网站建设1",
  "code": "companyWebsite",
  "bind": "0",
  "line": 0,
  "type": "normal",
  "status": "normal",
  "subStatus": "",
  "desc": "建立公司企业网站，可以更好对外展示。<br />",
  "PO": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "QD": {
    "id": 10,
    "account": "testManager",
    "avatar": "",
    "realname": "测试经理"
  },
  "RD": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "acl": "open",
  "whitelist": [],
  "reviewer": "",
  "createdBy": {
    "id": 2,
    "account": "productManager",
    "avatar": "",
    "realname": "产品经理"
  },
  "createdDate": "2012-06-05T01:57:07Z",
  "createdVersion": "",
  "order": 5,
  "deleted": "0",
  "stories": {
    "active": 5,
    "draft": 3,
    "": 0,
    "closed": 0,
    "changed": 0
  },
  "plans": 0,
  "releases": 0,
  "builds": 0,
  "cases": 5,
  "projects": 0,
  "executions": 0,
  "bugs": 5,
  "docs": 0,
  "progress": 0,
  "caseReview": false
}
```

---

## 7. 获取产品Bug列表

**Source**: https://www.zentao.net/book/api/720.html

#### 本篇目录

获取产品Bug列表
请求URL
请求头
请求响应
响应示例
GET
/products/id/bugs

### 获取产品Bug列表

#### 请求URL

https://xxx.com/api.php/v1/products/id/bugs

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| page | int | 是  | 当前页数 |
| ---- | --- | --- | -------- |

#### 响应示例

```json
{
  "page": 1,
  "total": 1,
  "limit": 20,
  "bugs": [
    {
      "id": 9,
      "project": 0,
      "product": 4,
      "branch": 0,
      "module": 0,
      "execution": 0,
      "plan": 0,
      "story": 0,
      "storyVersion": 1,
      "task": 0,
      "toTask": 0,
      "toStory": 0,
      "title": "Bug3",
      "keywords": "",
      "severity": 3,
      "pri": 0,
      "type": "",
      "os": "",
      "browser": "",
      "hardware": "",
      "found": "",
      "steps": "",
      "status": {
        "code": "active",
        "name": "激活"
      },
      "subStatus": "",
      "color": "",
      "confirmed": 0,
      "activatedCount": 0,
      "activatedDate": "1969-12-31T16:00:00Z",
      "feedbackBy": "",
      "notifyEmail": "",
      "mailto": null,
      "openedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "openedDate": "2021-12-01T01:25:42Z",
      "openedBuild": "主干",
      "assignedTo": null,
      "assignedDate": "1969-12-31T16:00:00Z",
      "deadline": "1970-01-01",
      "resolvedBy": null,
      "resolution": "",
      "resolvedBuild": "",
      "resolvedDate": "1969-12-31T16:00:00Z",
      "closedBy": null,
      "closedDate": "1969-12-31T16:00:00Z",
      "duplicateBug": 0,
      "linkBug": "",
      "case": 0,
      "caseVersion": 1,
      "result": 0,
      "repo": 0,
      "entry": "",
      "lines": "",
      "v1": "",
      "v2": "",
      "repoType": "",
      "testtask": 0,
      "lastEditedBy": null,
      "lastEditedDate": "1969-12-31T16:00:00Z",
      "deleted": false,
      "needconfirm": false
    }
  ]
}
```

---

## 7. 获取产品用例列表

**Source**: https://www.zentao.net/book/api/725.html

#### 本篇目录

获取产品用例列表
请求URL
请求头
请求响应
响应示例
GET
/products/id/testcases

### 获取产品用例列表

#### 请求URL

https://xxx.com/api.php/v1/products/id/testcases

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| page | int | 是  | 当前页数 |
| ---- | --- | --- | -------- |

#### 响应示例

```json
{
  "page": 1,
  "total": 6,
  "limit": 20,
  "testcases": [
    {
      "id": 10,
      "project": 0,
      "product": 1,
      "execution": 0,
      "branch": 0,
      "lib": 0,
      "module": 0,
      "path": 0,
      "story": 0,
      "storyVersion": 1,
      "title": "case1",
      "precondition": "",
      "keywords": "",
      "pri": 1,
      "type": "feature",
      "auto": "no",
      "frame": "",
      "stage": "",
      "howRun": "",
      "scriptedBy": "",
      "scriptedDate": null,
      "scriptStatus": "",
      "scriptLocation": "",
      "status": "normal",
      "subStatus": "",
      "color": "",
      "frequency": "1",
      "order": 0,
      "openedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "openedDate": "2021-12-05T15:05:16Z",
      "reviewedBy": null,
      "reviewedDate": null,
      "lastEditedBy": null,
      "lastEditedDate": null,
      "version": 1,
      "linkCase": "",
      "fromBug": 0,
      "fromCaseID": 0,
      "fromCaseVersion": 1,
      "deleted": false,
      "lastRunner": "",
      "lastRunDate": null,
      "lastRunResult": "",
      "storyTitle": null,
      "needconfirm": false,
      "bugs": 0,
      "results": 0,
      "caseFails": 0,
      "stepNumber": 1,
      "statusName": "正常"
    }
  ]
}
```
