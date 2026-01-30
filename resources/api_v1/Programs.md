# ZenTao Programs API


## 7. 获取项目集列表

**Source**: https://www.zentao.net/book/api/670.html

#### 本篇目录

获取项目集列表
请求URL
请求头
请求参数
请求响应
响应示例
GET
/programs

### 获取项目集列表

#### 请求URL

https://xxx.com/api.php/v1/programs

#### 请求头

| Token | String | 是  | 访问凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| order | String | 排序，默认order_asc；排序字段+下划线+asc/desc |
| ----- | ------ | --------------------------------------------- |

#### 请求响应

| programs | array | 是  | 项目集列表 |
| -------- | ----- | --- | ---------- |

#### 响应示例

```json
{
  "programs": [
    {
      "id": 6,
      "project": 0,
      "model": "",
      "type": "program",
      "lifetime": "sprint",
      "budget": "0",
      "budgetUnit": "CNY",
      "attribute": "",
      "percent": 0,
      "milestone": "0",
      "output": "",
      "auth": "",
      "parent": 0,
      "path": ",6,",
      "grade": 1,
      "name": "企业管理",
      "code": "",
      "begin": "2021-06-05",
      "end": "2022-06-04",
      "realBegan": "2021-12-01",
      "realEnd": "2021-12-01",
      "days": 0,
      "status": "doing",
      "subStatus": "",
      "pri": "1",
      "desc": "",
      "version": 0,
      "parentVersion": 0,
      "planDuration": 0,
      "realDuration": 0,
      "openedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "openedDate": "2021-04-28T03:22:04Z",
      "openedVersion": "15.0.rc3",
      "lastEditedBy": "",
      "lastEditedDate": "2021-11-30T16:00:00Z",
      "closedBy": null,
      "closedDate": "2021-11-30T16:00:00Z",
      "canceledBy": null,
      "canceledDate": "2021-11-30T16:00:00Z",
      "PO": null,
      "PM": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
      },
      "QD": null,
      "RD": null,
      "team": "企业管理",
      "acl": "open",
      "whitelist": ",",
      "order": 30,
      "deleted": false,
      "progress": 0
    }
  ]
}
```

---

## 7. 修改项目集

**Source**: https://www.zentao.net/book/api/671.html

#### 本篇目录

修改项目集
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/programs/id

### 修改项目集

#### 请求URL

https://xxx.com/api.php/v1/programs/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 否  | 项目名称 |
| ---- | ------ | --- | -------- |

#### 请求示例

```json
{
  "name": "项目集",
  "PM": "admin"
}
```

#### 请求响应

| id  | int | 是  |
| --- | --- | --- |

#### 响应示例

```json
{
  "id": 12,
  "project": 0,
  "model": "",
  "type": "program",
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
  "name": "项目集",
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

## 7. 获取项目集详情

**Source**: https://www.zentao.net/book/api/672.html

#### 本篇目录

获取项目集详情
请求URL
请求头
请求响应
响应示例
GET
/programs/id

### 获取项目集详情

#### 请求URL

https://xxx.com/api.php/v1/programs/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 项目集ID |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 14,
  "project": 0,
  "model": "",
  "type": "program",
  "lifetime": "",
  "budget": "11111",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 0,
  "path": ",14,",
  "grade": 1,
  "name": "测试项目集",
  "code": "",
  "begin": "2021-11-26",
  "end": "2021-12-26",
  "realBegan": null,
  "realEnd": null,
  "days": 0,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "openedDate": "2021-11-26T10:05:51Z",
  "openedVersion": "",
  "lastEditedBy": "",
  "lastEditedDate": null,
  "closedBy": null,
  "closedDate": null,
  "canceledBy": null,
  "canceledDate": null,
  "PO": null,
  "PM": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "QD": null,
  "RD": null,
  "team": "",
  "acl": "private",
  "whitelist": [],
  "order": 70,
  "deleted": false
}
```

---

## 7. 创建项目集

**Source**: https://www.zentao.net/book/api/674.html

#### 本篇目录

创建项目集
请求URL
请求头
请求体
请求响应
响应示例
POST
/programs

### 创建项目集

#### 请求URL

https://xxx.com/api.php/v1/programs

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| name | string | 否  | 项目名称 |
| ---- | ------ | --- | -------- |

#### 请求响应

| id  | int | 是  |
| --- | --- | --- |

#### 响应示例

```json
{
  "id": 43,
  "project": 0,
  "model": "",
  "type": "program",
  "lifetime": "",
  "budget": "0",
  "budgetUnit": "CNY",
  "attribute": "",
  "percent": 0,
  "milestone": "0",
  "output": "",
  "auth": "",
  "parent": 0,
  "path": ",43,",
  "grade": 1,
  "name": "项目集21",
  "code": "",
  "begin": "2021-09-11",
  "end": "2021-12-31",
  "realBegan": null,
  "realEnd": null,
  "days": 0,
  "status": "wait",
  "subStatus": "",
  "pri": "1",
  "desc": "",
  "version": 0,
  "parentVersion": 0,
  "planDuration": 0,
  "realDuration": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "openedDate": "2021-12-03T02:07:36Z",
  "openedVersion": "",
  "lastEditedBy": "",
  "lastEditedDate": null,
  "closedBy": null,
  "closedDate": null,
  "canceledBy": null,
  "canceledDate": null,
  "PO": null,
  "PM": null,
  "QD": null,
  "RD": null,
  "team": "",
  "acl": "private",
  "whitelist": [
    {
      "id": 1,
      "account": "admin",
      "avatar": "",
      "realname": "管理员"
    }
  ],
  "order": 215,
  "deleted": false
}
```
