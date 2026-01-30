# ZenTao Tickets API


## 7. 获取工单列表

**Source**: https://www.zentao.net/book/api/1266.html

#### 本篇目录

获取工单列表
请求URL
请求头
请求参数
请求响应
响应示例
GET
/tickets

### 获取工单列表

#### 请求URL

https://xxx.com/api.php/v1/tickets

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| <br/> | <br/> |
| ----- | ----- |

#### 请求响应

| <br/> | <br/> | <br/> | <br/> |
| ----- | ----- | ----- | ----- |

#### 响应示例

```json
{
    "page": 1,
    "total": 7,
    "limit": 20,
    "tickets": [
        {
            "id": 7,
            "product": 80,
            "module": 80,
            "title": "sgm GIAO",
            "type": "",
            "desc": "",
            "openedBuild": "",
            "feedback": 0,
            "assignedTo": null,
            "assignedDate": "0000-00-00 00:00:00",
            "realStarted": "0000-00-00 00:00:00",
            "startedBy": "",
            "startedDate": "0000-00-00 00:00:00",
            "deadline": "-0001-11-29T16:00:00Z",
            "pri": 0,
            "estimate": 0,
            "left": 0,
            "status": "wait",
            "openedBy": {
                "id": 4,
                "account": "admin",
                "avatar": "/data/upload/1/202104/02151445087773h0",
                "realname": "管理员"
            },
            "openedDate": "2022-12-21T07:45:54Z",
            "activatedCount": 0,
            "activatedBy": null,
            "activatedDate": null,
            "closedBy": null,
            "closedDate": null,
            "closedReason": "",
            "finishedBy": null,
            "finishedDate": null,
            "resolvedBy": "",
            "resolvedDate": "0000-00-00 00:00:00",
            "resolution": "",
            "editedBy": null,
            "editedDate": null,
            "keywords": "",
            "repeatTicket": 0,
            "mailto": [],
            "deleted": false,
            "consumed": 0,
        }
}
```

---

## 7. 获取工单详情

**Source**: https://www.zentao.net/book/api/1267.html

#### 本篇目录

获取工单详情
请求URL
请求头
请求响应
响应示例
GET
/tickets/id

### 获取工单详情

#### 请求URL

https://xxx.com/api.php/v1/tickets/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

####

#### 请求响应

| <br/> | <br/> | <br/> | <br/> |
| ----- | ----- | ----- | ----- |

#### 响应示例

```json
{
    "id": 5,
    "product": 80,
    "module": 80,
    "title": "测试工单",
    "type": "",
    "desc": "",
    "openedBuild": "",
    "feedback": 0,
    "assignedTo": null,
    "assignedDate": null,
    "realStarted": "0000-00-00 00:00:00",
    "startedBy": "",
    "startedDate": "",
    "deadline": null,
    "pri": 0,
    "estimate": 0,
    "left": 0,
    "status": "wait",
    "openedBy": {
        "id": 4,
        "account": "admin",
        "avatar": "/data/upload/1/202104/02151445087773h0",
        "realname": "管理员"
    },
    "openedDate": "2022-12-21T07:43:33Z",
    "activatedCount": 0,
    "activatedBy": "",
    "activatedDate": null,
    "closedBy": null,
    "closedDate": null,
    "closedReason": "",
    "finishedBy": "",
    "finishedDate": "",
    "resolvedBy": null,
    "resolvedDate": null,
    "resolution": "",
    "editedBy": "admin",
    "editedDate": "2022-12-22 10:29:27",
    "keywords": "",
    "repeatTicket": 0,
    "mailto": [],
    "deleted": false,
    "consumed": 0,
    "createFiles": [],
    "finishFiles": [],
    "productName": null,
    "moduleName": "/",
    "actions": [
        {
            "id": 179347,
            "objectType": "ticket",
            "objectID": 5,
            "product": ",80,",
            "project": "0",
            "execution": 0,
            "actor": "管理员",
            "action": "opened",
            "date": "2022-12-21 15:43:33",
            "comment": "",
            "extra": "",
            "efforted": 0,
            "read": "0",
            "vision": "rnd",
            "history": [],
            "desc": "2022-12-21 15:43:33, 由 <strong>管理员</strong> 创建。\n"
        }
        }
    ]
}
```

---

## 7. 修改工单

**Source**: https://www.zentao.net/book/api/1268.html

#### 本篇目录

修改工单
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/tickets/id

### 修改工单

#### 请求URL

https://xxx.com/api.php/v1/tickets/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| 否  |
| --- |

#### 请求示例

```json
{
  "title": "test",
  "desc": "edit test"
}
```

####

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 5,
  "product": 80,
  "module": 80,
  "title": "test",
  "type": "",
  "desc": "edit test",
  "openedBuild": "",
  "feedback": 0,
  "assignedTo": null,
  "assignedDate": "",
  "realStarted": "0000-00-00 00:00:00",
  "startedBy": "",
  "startedDate": "",
  "deadline": null,
  "pri": 0,
  "estimate": 0,
  "left": 0,
  "status": "wait",
  "openedBy": {
    "id": 4,
    "account": "admin",
    "avatar": "/data/upload/1/202104/02151445087773h0",
    "realname": "管理员"
  },
  "openedDate": "2022-12-21T07:43:33Z",
  "activatedCount": 0,
  "activatedBy": null,
  "activatedDate": null,
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "finishedBy": null,
  "finishedDate": null,
  "resolvedBy": "",
  "resolvedDate": "",
  "resolution": "",
  "editedBy": {
    "id": 4,
    "account": "admin",
    "avatar": "/data/upload/1/202104/02151445087773h0",
    "realname": "管理员"
  },
  "editedDate": "2022-12-22T06:02:26Z",
  "keywords": "",
  "repeatTicket": 0,
  "mailto": [],
  "deleted": false,
  "consumed": 0,
  "sgm": "",
  "sgmA": "",
  "createFiles": [],
  "finishFiles": []
}
```

---

## 7. 创建工单

**Source**: https://www.zentao.net/book/api/1269.html

#### 本篇目录

创建工单
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tickets

### 创建工单

#### 请求URL

https://xxx.com/api.php/v1/tickets

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| 是  |
| --- |

#### 请求示例

```json
{
  "product": 2,
  "title": "create test feedback"
}
```

####

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 8,
  "product": 2,
  "module": 2,
  "title": "create test ticket",
  "type": "",
  "desc": "",
  "openedBuild": "",
  "feedback": 0,
  "assignedTo": null,
  "assignedDate": "",
  "realStarted": "0000-00-00 00:00:00",
  "startedBy": "",
  "startedDate": "",
  "deadline": null,
  "pri": 0,
  "estimate": 0,
  "left": 0,
  "status": "wait",
  "openedBy": {
    "id": 4,
    "account": "admin",
    "avatar": "/data/upload/1/202104/02151445087773h0",
    "realname": "管理员"
  },
  "openedDate": "2022-12-22T05:49:43Z",
  "activatedCount": 0,
  "activatedBy": null,
  "activatedDate": null,
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "finishedBy": null,
  "finishedDate": null,
  "resolvedBy": "",
  "resolvedDate": "",
  "resolution": "",
  "editedBy": null,
  "editedDate": null,
  "keywords": "",
  "repeatTicket": 0,
  "mailto": [],
  "deleted": false,
  "consumed": 0,
  "createFiles": [],
  "finishFiles": []
}
```
