# ZenTao Executions API


## 7. 获取执行版本列表

**Source**: https://www.zentao.net/book/api/705.html

#### 本篇目录

获取执行版本列表
请求URL
请求头
请求响应
响应示例
GET
/executions/id/builds

### 获取执行版本列表

#### 请求URL

https://xxx.com/api.php/v1/executions/id/builds

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

## 7. 创建执行

**Source**: https://www.zentao.net/book/api/711.html

#### 本篇目录

创建执行
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/projects/id/executions

### 创建执行

#### 请求URL

https://xxx.com/api.php/v1/projects/id/executions

#### 请求头

| Token | String | 是  | 认证凭证 |
| ----- | ------ | --- | -------- |

#### 请求体

| project | int | 是  | 所属项目 |
| ------- | --- | --- | -------- |

#### 请求示例

```json
{
  "name": "测试执行1",
  "code": "test1",
  "begin": "2021-12-01",
  "end": "2021-12-11",
  "days": 10
}
```

#### 请求响应

| id  | int | 是  | 执行ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 40,
  "project": 12,
  "model": "",
  "type": "sprint",
  "lifetime": "",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 12,
  "path": ",12,40,",
  "grade": 1,
  "name": "测试执行1",
  "code": "test1",
  "begin": "2021-12-01",
  "end": "2021-12-11",
  "realBegan": "0000-00-00",
  "realEnd": "0000-00-00",
  "days": 100,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-11-28T15:37:59Z",
  "openedVersion": "15.8",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-28T15:37:59Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "",
  "QD": "",
  "RD": "",
  "team": "测试执行1",
  "acl": "private",
  "whitelist": ",",
  "order": 200,
  "deleted": "0",
  "totalHours": 700,
  "totalEstimate": 0,
  "totalConsumed": 0,
  "totalLeft": 0
}
```

---

## 7. 查看执行详情

**Source**: https://www.zentao.net/book/api/712.html

#### 本篇目录

查看执行详情
请求URL
请求头
请求响应
响应示例
GET
/executions/id

### 查看执行详情

#### 请求URL

https://xxx.com/api.php/v1/executions/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 执行ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 40,
  "project": 12,
  "model": "",
  "type": "sprint",
  "lifetime": "",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 12,
  "path": ",12,40,",
  "grade": 1,
  "name": "测试执行1111111",
  "code": "test1111111",
  "begin": "2021-12-01",
  "end": "2021-12-11",
  "realBegan": "0000-00-00",
  "realEnd": "0000-00-00",
  "days": 100,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-11-28T15:37:59Z",
  "openedVersion": "15.8",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-28T15:37:59Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "",
  "QD": "",
  "RD": "",
  "team": "测试执行1111111",
  "acl": "private",
  "whitelist": ",",
  "order": 200,
  "deleted": "0",
  "totalHours": 700,
  "totalEstimate": 0,
  "totalConsumed": 0,
  "totalLeft": 0
}
```

---

## 7. 修改执行

**Source**: https://www.zentao.net/book/api/713.html

#### 本篇目录

修改执行
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/executions/id

### 修改执行

#### 请求URL

https://xxx.com/api.php/v1/executions/id

#### 请求头

| Token | String | 是  | 认证凭证 |
| ----- | ------ | --- | -------- |

#### 请求体

| project | int | 是  | 所属项目 |
| ------- | --- | --- | -------- |

#### 请求示例

```json
{
  "name": "测试执行1",
  "code": "test1",
  "begin": "2021-12-01",
  "end": "2021-12-11",
  "days": 10
}
```

#### 请求响应

| id  | int | 是  | 执行ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 40,
  "project": 12,
  "model": "",
  "type": "sprint",
  "lifetime": "",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 12,
  "path": ",12,40,",
  "grade": 1,
  "name": "测试执行1",
  "code": "test1",
  "begin": "2021-12-01",
  "end": "2021-12-11",
  "realBegan": "0000-00-00",
  "realEnd": "0000-00-00",
  "days": 100,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": "admin",
  "openedDate": "2021-11-28T15:37:59Z",
  "openedVersion": "15.8",
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-28T15:37:59Z",
  "closedBy": "",
  "closedDate": null,
  "canceledBy": "",
  "canceledDate": null,
  "PO": "",
  "PM": "",
  "QD": "",
  "RD": "",
  "team": "测试执行1",
  "acl": "private",
  "whitelist": ",",
  "order": 200,
  "deleted": "0",
  "totalHours": 700,
  "totalEstimate": 0,
  "totalConsumed": 0,
  "totalLeft": 0
}
```

---

## 7. 获取执行任务列表

**Source**: https://www.zentao.net/book/api/715.html

#### 本篇目录

获取执行任务列表
请求URL
请求头
请求响应
响应示例
GET
/executions/id/tasks

### 获取执行任务列表

#### 请求URL

https://xxx.com/api.php/v1/executions/id/tasks

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
  "limit": 100,
  "tasks": [
    {
      "id": 18,
      "project": 12,
      "parent": 0,
      "execution": 13,
      "module": 0,
      "design": 0,
      "story": 0,
      "storyVersion": 1,
      "designVersion": 0,
      "fromBug": 0,
      "name": "task1",
      "type": "devel",
      "pri": 3,
      "estimate": 0,
      "consumed": 2,
      "left": 0,
      "deadline": null,
      "status": "done",
      "subStatus": "",
      "color": "",
      "mailto": [],
      "desc": "",
      "version": 1,
      "openedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "openedDate": "2021-11-29T02:33:47Z",
      "assignedTo": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "assignedDate": "2021-11-29T02:52:25Z",
      "estStarted": "0000-00-00",
      "realStarted": "2021-11-29T02:50:00Z",
      "finishedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "finishedDate": "2021-11-29T02:52:17Z",
      "finishedList": "",
      "canceledBy": null,
      "canceledDate": null,
      "closedBy": null,
      "closedDate": null,
      "planDuration": 0,
      "realDuration": 0,
      "closedReason": "",
      "lastEditedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "lastEditedDate": "2021-11-29T02:52:25Z",
      "activatedDate": "0000-00-00",
      "deleted": false,
      "storyID": null,
      "storyTitle": null,
      "product": null,
      "branch": null,
      "latestStoryVersion": null,
      "storyStatus": null,
      "assignedToRealName": "管理员",
      "needConfirm": false,
      "progress": 100
    }
  ]
}
```

---

## 7. 执行用例

**Source**: https://www.zentao.net/book/api/962.html

#### 本篇目录

执行用例
请求URL
请求头
请求参数
请求体
请求示例
请求响应
POST
/testcases/id/results

### 执行用例

#### 请求URL

https://xxx.com/api.php/v1/testcases/id/results

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| testtask | int | 否  | 测试单的ID，默认为0。用于标识测试用例在测试单中执行 |
| -------- | --- | --- | --------------------------------------------------- |

#### 请求体

| steps | array | 是  | 用例结果和描述，结果可选"n/a | fail | blocked | pass" |
| ----- | ----- | --- | ---------------------------- | ---- | ------- | ----- |

#### 请求示例

```json
{
  "steps": [
    { "result": "n/a", "real": "忽略" },
    { "result": "fail", "real": "失败" },
    { "result": "blocked", "real": "阻塞" },
    { "result": "pass", "real": "成功" }
  ]
}
```

#### 请求响应

| message | string | 是  | 失败信息，若成功则返回空数组 |
| ------- | ------ | --- | ---------------------------- |
