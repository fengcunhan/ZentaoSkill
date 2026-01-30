# ZenTao QA API


## 7. 创建用例

**Source**: https://www.zentao.net/book/api/726.html

#### 本篇目录

创建用例
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/products/id/testcases

### 创建用例

#### 请求URL

https://xxx.com/api.php/v1/products/id/testcases

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "title": "case1",
  "pri": 1,
  "steps": [
    {
      "desc": "步骤1",
      "expect": "结果1"
    }
  ],
  "type": "feature"
}
```

#### 请求响应

| id  | int | 是  | 用例ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 8,
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
  "openedBy": "admin",
  "openedDate": "2021-11-29T07:18:29Z",
  "reviewedBy": "",
  "reviewedDate": null,
  "lastEditedBy": "",
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
  "toBugs": [],
  "steps": [
    {
      "id": 5,
      "parent": 0,
      "case": 8,
      "version": 1,
      "type": "step",
      "desc": "步骤1",
      "expect": "结果1"
    }
  ],
  "files": [],
  "currentVersion": 1
}
```

---

## 7. 获取用例详情

**Source**: https://www.zentao.net/book/api/727.html

#### 本篇目录

获取用例详情
请求URL
请求头
请求响应
响应示例
GET
/testcases/id

### 获取用例详情

#### 请求URL

https://xxx.com/api.php/v1/testcases/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 用例ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 9,
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
  "openedDate": "2021-11-29T07:24:42Z",
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
  "toBugs": [],
  "steps": [
    {
      "id": 6,
      "parent": 0,
      "case": 9,
      "version": 1,
      "type": "step",
      "desc": "步骤1",
      "expect": "结果1"
    }
  ],
  "files": [],
  "currentVersion": 1,
  "caseFails": 0
}
```

---

## 7. 修改用例

**Source**: https://www.zentao.net/book/api/728.html

#### 本篇目录

修改用例
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/testcases/id

### 修改用例

#### 请求URL

https://xxx.com/api.php/v1/testcases/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "title": "case1",
  "pri": 1,
  "steps": [
    {
      "desc": "步骤1",
      "expect": "结果1"
    }
  ],
  "type": "feature"
}
```

#### 请求响应

| id  | int | 是  | 用例ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 9,
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
  "openedDate": "2021-11-29T07:24:42Z",
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
  "toBugs": [],
  "steps": [
    {
      "id": 6,
      "parent": 0,
      "case": 9,
      "version": 1,
      "type": "step",
      "desc": "步骤1",
      "expect": "结果1"
    }
  ],
  "files": [],
  "currentVersion": 1,
  "caseFails": 0
}
```

---

## 7. 获取测试单列表

**Source**: https://www.zentao.net/book/api/730.html

#### 本篇目录

获取测试单列表
请求URL
请求头
请求参数
请求响应
响应示例
GET
/testtasks

### 获取测试单列表

#### 请求URL

https://xxx.com/api.php/v1/testtasks

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| page | String | 当前页数，默认为1 |
| ---- | ------ | ----------------- |

#### 请求响应

| page | int | 是  | 当前页面 |
| ---- | --- | --- | -------- |

#### 响应示例

```json
{
  "page": 1,
  "total": 1,
  "limit": 20,
  "testtasks": [
    {
      "id": 1,
      "project": 0,
      "product": 1,
      "name": "企业网站第一期测试任务",
      "execution": 1,
      "build": "1",
      "type": "",
      "owner": "testManager",
      "pri": 0,
      "begin": "2020-06-05",
      "end": "2021-06-21",
      "realFinishedDate": null,
      "mailto": "",
      "desc": "",
      "report": "",
      "status": "wait",
      "testreport": 0,
      "auto": "no",
      "subStatus": "",
      "deleted": "0",
      "productName": "公司企业网站建设1",
      "executionName": "企业网站第一期",
      "buildName": "第一期版本",
      "branch": 0
    }
  ]
}
```

---

## 7. 获取测试单详情

**Source**: https://www.zentao.net/book/api/732.html

#### 本篇目录

获取测试单详情
请求URL
请求头
请求响应
GET
/testtasks/id

### 获取测试单详情

#### 请求URL

https://xxx.com/api.php/v1/testtasks/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 测试单编号 |
| --- | --- | --- | ---------- |
