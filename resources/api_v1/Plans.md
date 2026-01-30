# ZenTao Plans API


## 7. 获取产品计划列表

**Source**: https://www.zentao.net/book/api/680.html

#### 本篇目录

获取产品计划列表
请求URL
请求头
请求响应
响应示例
GET
/products/id/plans

### 获取产品计划列表

#### 请求URL

https://xxx.com/api.php/v1/products/id/plans

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
  "limit": 1,
  "plans": [
    {
      "id": 1,
      "product": 1,
      "branch": 0,
      "parent": 0,
      "title": "1.0beta",
      "status": "wait",
      "desc": "",
      "begin": "2022-11-09",
      "end": "2030-01-01",
      "order": "",
      "closedReason": "",
      "deleted": false,
      "stories": 2,
      "bugs": 0,
      "hour": 0,
      "projects": {
        "2": {
          "project": 2,
          "name": "计划1.0beta迭代"
        }
      },
      "expired": false
    }
  ]
}
```

---

## 7. 产品计划关联需求

**Source**: https://www.zentao.net/book/api/685.html

#### 本篇目录

产品计划关联需求
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/productplans/id/linkstories

### 产品计划关联需求

#### 请求URL

https://xxx.com/api.php/v1/productplans/id/linkstories

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| stories | array | 否  | 新增关联的需求，比如 [1, 2] |
| ------- | ----- | --- | --------------------------- |

#### 请求示例

```json
{
  "stories": [11]
}
```

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 4,
  "product": 4,
  "branch": 2,
  "parent": 0,
  "title": "分支2计划",
  "desc": "",
  "begin": "2021-11-30",
  "end": "2021-12-06",
  "order": "",
  "deleted": false,
  "stories": [
    {
      "story": 11,
      "plan": "4",
      "order": 1,
      "id": 11,
      "parent": 0,
      "product": 4,
      "branch": 2,
      "module": 22,
      "source": "",
      "sourceNote": "",
      "fromBug": 0,
      "title": "分支2需求",
      "keywords": "",
      "type": "story",
      "category": "feature",
      "pri": 3,
      "estimate": 0,
      "status": "active",
      "subStatus": "",
      "color": "",
      "stage": "planned",
      "stagedBy": "",
      "mailto": "",
      "openedBy": "admin",
      "openedDate": "2021-11-23 15:37:37",
      "assignedTo": "",
      "assignedDate": "0000-00-00 00:00:00",
      "lastEditedBy": "",
      "lastEditedDate": "0000-00-00 00:00:00",
      "reviewedBy": "",
      "reviewedDate": "0000-00-00 00:00:00",
      "closedBy": "",
      "closedDate": "0000-00-00 00:00:00",
      "closedReason": "",
      "toBug": 0,
      "childStories": "",
      "linkStories": "",
      "duplicateStory": 0,
      "version": 1,
      "URChanged": "0",
      "deleted": "0"
    }
  ],
  "bugs": []
}
```

---

## 7. 产品计划取消关联需求

**Source**: https://www.zentao.net/book/api/686.html

#### 本篇目录

产品计划取消关联需求
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/productplans/id/unlinkstories

### 产品计划取消关联需求

#### 请求URL

https://xxx.com/api.php/v1/productplans/id/unlinkstories

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| stories | array | 是  | 取消关联的需求ID，比如 [1, 2] |
| ------- | ----- | --- | ----------------------------- |

#### 请求示例

```json
{
  "stories": [11]
}
```

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 4,
  "product": 4,
  "branch": 2,
  "parent": 0,
  "title": "分支2计划",
  "desc": "",
  "begin": "2021-11-30",
  "end": "2021-12-06",
  "order": "",
  "deleted": false,
  "stories": [],
  "bugs": []
}
```

---

## 7. 产品计划关联Bug

**Source**: https://www.zentao.net/book/api/687.html

#### 本篇目录

产品计划关联Bug
请求URL
请求体
请求示例
请求响应
响应示例
POST
/productplans/id/linkbugs

### 产品计划关联Bug

#### 请求URL

https://xxx.com/api.php/v1/productplans/id/linkbugs

#### 请求体

| bugs | array | 是  | 关联的Bug ID，比如 [1, 2] |
| ---- | ----- | --- | ------------------------- |

#### 请求示例

```json
{
  "bugs": [7]
}
```

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 4,
  "product": 4,
  "branch": 2,
  "parent": 0,
  "title": "分支2计划",
  "desc": "",
  "begin": "2021-11-30",
  "end": "2021-12-06",
  "order": "",
  "deleted": false,
  "stories": [],
  "bugs": [
    {
      "id": 7,
      "project": 0,
      "product": 4,
      "branch": 0,
      "module": 0,
      "execution": 0,
      "plan": 4,
      "story": 0,
      "storyVersion": 1,
      "task": 0,
      "toTask": 0,
      "toStory": 0,
      "title": "Bug1",
      "keywords": "",
      "severity": 3,
      "pri": 3,
      "type": "codeerror",
      "os": "",
      "browser": "",
      "hardware": "",
      "found": "",
      "steps": "<p>[步骤]</p>\n<br />\n<p>[结果]</p>\n<br />\n<p>[期望]</p>\n<br />",
      "status": "active",
      "subStatus": "",
      "color": "",
      "confirmed": 0,
      "activatedCount": 0,
      "activatedDate": "0000-00-00 00:00:00",
      "mailto": "",
      "openedBy": "admin",
      "openedDate": "2021-12-01 09:25:23",
      "openedBuild": "trunk",
      "assignedTo": "",
      "assignedDate": "0000-00-00 00:00:00",
      "deadline": "0000-00-00",
      "resolvedBy": "",
      "resolution": "",
      "resolvedBuild": "",
      "resolvedDate": "0000-00-00 00:00:00",
      "closedBy": "",
      "closedDate": "0000-00-00 00:00:00",
      "duplicateBug": 0,
      "linkBug": "",
      "case": 0,
      "caseVersion": 0,
      "result": 0,
      "repo": 0,
      "entry": "",
      "lines": "",
      "v1": "",
      "v2": "",
      "repoType": "",
      "testtask": 0,
      "lastEditedBy": "",
      "lastEditedDate": "0000-00-00 00:00:00",
      "deleted": "0"
    }
  ]
}
```

---

## 7. 产品计划取消关联Bug

**Source**: https://www.zentao.net/book/api/688.html

#### 本篇目录

产品计划取消关联Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/productplans/id/unlinkbugs

### 产品计划取消关联Bug

#### 请求URL

https://xxx.com/api.php/v1/productplans/id/unlinkbugs

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| bugs | array | 是  | 取消关联的Bug ID，比如 [1, 2] |
| ---- | ----- | --- | ----------------------------- |

#### 请求示例

```json
{
  "bugs": [7]
}
```

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 4,
  "product": 4,
  "branch": 2,
  "parent": 0,
  "title": "分支2计划",
  "desc": "",
  "begin": "2021-11-30",
  "end": "2021-12-06",
  "order": "",
  "deleted": false,
  "stories": [],
  "bugs": []
}
```
