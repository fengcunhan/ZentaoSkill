# ZenTao Projects API


## 7. 获取项目列表

**Source**: https://www.zentao.net/book/api/699.html

#### 本篇目录

获取项目列表
请求URL
请求头
请求参数
请求响应
响应示例
GET
/projects

### 获取项目列表

#### 请求URL

https://xxx.com/api.php/v1/projects

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| page | String | 第几页，默认为1 |
| ---- | ------ | --------------- |

#### 请求响应

| page | int | 是  | 页数 |
| ---- | --- | --- | ---- |

#### 响应示例

```json
{
  "page": 1,
  "total": 2,
  "limit": 20,
  "projects": [
    {
      "id": 7,
      "name": "企业管理系统",
      "code": "",
      "model": "scrum",
      "type": "project",
      "budget": "0",
      "budgetUnit": "CNY",
      "parent": 6,
      "begin": "2021-06-05",
      "end": "2022-06-04",
      "status": "doing",
      "openedBy": "admin",
      "openedDate": "2021-04-28T03:22:04Z",
      "PM": "projectManager",
      "progress": 33
    },
    {
      "id": 8,
      "name": "分支项目",
      "code": "bb",
      "model": "scrum",
      "type": "project",
      "budget": "",
      "budgetUnit": "CNY",
      "parent": 6,
      "begin": "2021-11-23",
      "end": "2021-12-23",
      "status": "wait",
      "openedBy": "admin",
      "openedDate": "2021-11-23T07:45:16Z",
      "PM": "",
      "progress": 0
    }
  ]
}
```

---

## 7. 创建项目

**Source**: https://www.zentao.net/book/api/700.html

#### 本篇目录

创建项目
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/projects

### 创建项目

#### 请求URL

https://xxx.com/api.php/v1/projects

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 是  | 项目名称 |
| ---- | ------ | --- | -------- |

#### 请求示例

```json
{
  "name": "test",
  "code": "test",
  "begin": "2021-01-01",
  "end": "2022-01-01",
  "products": [1]
}
```

#### 请求响应

| id  | int | 是  | 项目编号 |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 9,
  "model": "scrum",
  "type": "project",
  "lifetime": "",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 0,
  "path": ",9,",
  "grade": 1,
  "name": "test",
  "code": "test",
  "begin": "2021-01-01",
  "end": "2022-01-01",
  "realBegan": "0000-00-00",
  "realEnd": "0000-00-00",
  "days": 0,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-11-25T09:12:30Z",
  "openedVersion": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-25T09:12:30Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "",
  "QD": "",
  "RD": "",
  "team": "test",
  "acl": "private",
  "whitelist": ",",
  "order": 45,
  "deleted": "0"
}
```

---

## 7. 获取项目详情

**Source**: https://www.zentao.net/book/api/701.html

#### 本篇目录

获取项目详情
请求URL
请求头
请求响应
响应示例
GET
/projects/id

### 获取项目详情

#### 请求URL

https://xxx.com/api.php/v1/projects/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 项目编号 |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 7,
  "project": 0,
  "model": "scrum",
  "type": "project",
  "lifetime": "sprint",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "extend",
  "parent": 6,
  "path": ",6,7,",
  "grade": 2,
  "name": "企业管理系统",
  "code": "",
  "begin": "2021-06-05",
  "end": "2022-06-04",
  "realBegan": null,
  "realEnd": null,
  "days": 0,
  "status": "doing",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-04-28T03:22:04Z",
  "openedVersion": "15.0.rc3",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-04-28T03:22:04Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "projectManager",
  "QD": "",
  "RD": "",
  "team": "",
  "acl": "open",
  "whitelist": ",tester3,admin",
  "order": 35,
  "deleted": false,
  "caseReview": false
}
```

---

## 7. 修改项目

**Source**: https://www.zentao.net/book/api/702.html

#### 本篇目录

修改项目
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/projects/id

### 修改项目

#### 请求URL

https://xxx.com/api.php/v1/projects/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 否  | 项目名称 |
| ---- | ------ | --- | -------- |

#### 请求示例

```json
{
  "name": "修改项目",
  "PM": "admin"
}
```

#### 请求响应

| id  | int | 是  | 项目名称 |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 12,
  "project": 0,
  "model": "scrum",
  "type": "project",
  "lifetime": "",
  "budget": "",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "extend",
  "parent": 0,
  "path": ",12,",
  "grade": 1,
  "name": "修改项目",
  "code": "tt",
  "begin": "2021-11-26",
  "end": "2021-12-26",
  "realBegan": "0000-00-00",
  "realEnd": "0000-00-00",
  "days": 21,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-11-26T02:27:15Z",
  "openedVersion": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-26T02:33:18Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "admin",
  "QD": "",
  "RD": "",
  "team": "修改项目",
  "acl": "private",
  "whitelist": ",",
  "order": 60,
  "deleted": "0"
}
```

---

## 7. 获取项目版本列表

**Source**: https://www.zentao.net/book/api/704.html

#### 本篇目录

获取项目版本列表
请求URL
请求头
请求响应
响应示例
GET
/projects/id/builds

### 获取项目版本列表

#### 请求URL

https://xxx.com/api.php/v1/projects/id/builds

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| total | int | 是  | 版本总数 |
| ----- | --- | --- | -------- |

#### 响应示例

```json
{
  "total": 1,
  "builds": [
    {
      "id": 2,
      "project": 12,
      "product": 5,
      "branch": 0,
      "execution": 40,
      "name": "1111111",
      "scmPath": "",
      "filePath": "",
      "date": "2021-12-01",
      "stories": [],
      "bugs": [],
      "builder": "admin",
      "desc": "",
      "deleted": false,
      "executionName": "测试执行1111111",
      "executionID": 40,
      "productName": "测试",
      "branchName": ""
    }
  ]
}
```

---

## 7. 获取项目的执行列表

**Source**: https://www.zentao.net/book/api/710.html

#### 本篇目录

获取项目的执行列表
请求URL
请求头
请求响应
响应示例
GET
/projects/id/executions

### 获取项目的执行列表

#### 请求URL

https://xxx.com/api.php/v1/projects/id/executions

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
  "executions": [
    {
      "id": 13,
      "name": "迭代1",
      "project": 12,
      "code": "sprint1",
      "type": "sprint",
      "parent": 12,
      "begin": "2021-11-26",
      "end": "2021-12-02",
      "status": "wait",
      "openedBy": "admin",
      "openedDate": "2021-11-26T02:42:22Z",
      "progress": 0
    }
  ]
}
```

---

## 7. 获取项目的测试单

**Source**: https://www.zentao.net/book/api/731.html

#### 本篇目录

获取项目的测试单
请求URL
请求头
请求响应
响应示例
GET
/projects/id/testtasks

### 获取项目的测试单

#### 请求URL

https://xxx.com/api.php/v1/projects/id/testtasks

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

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
