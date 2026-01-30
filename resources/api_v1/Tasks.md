# ZenTao Tasks API


## 7. 创建任务

**Source**: https://www.zentao.net/book/api/716.html

#### 本篇目录

创建任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/executions/id/tasks

### 创建任务

#### 请求URL

https://xxx.com/api.php/v1/executions/id/tasks

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| module | int | 否  | 所属模块 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "name": "testtt",
  "assignedTo": "admin",
  "type": "devel",
  "estStarted": "2021-12-01",
  "deadline": "2021-12-31"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 23,
  "project": 12,
  "parent": 0,
  "execution": 55,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "name": "testttt",
  "type": "devel",
  "pri": 0,
  "estimate": 0,
  "consumed": 0,
  "left": 0,
  "deadline": "2021-12-31",
  "status": "wait",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "openedDate": "2021-12-05T12:54:30Z",
  "assignedTo": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "assignedDate": "2021-12-05T12:54:30Z",
  "estStarted": "2021-12-01",
  "realStarted": null,
  "finishedBy": null,
  "finishedDate": null,
  "finishedList": "",
  "canceledBy": null,
  "canceledDate": null,
  "closedBy": null,
  "closedDate": null,
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": null,
  "lastEditedDate": null,
  "activatedDate": "",
  "deleted": false,
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "管理员",
  "children": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 0
}
```

---

## 7. 获取任务详情

**Source**: https://www.zentao.net/book/api/717.html

#### 本篇目录

获取任务详情
请求URL
请求头
请求响应
响应示例
GET
/tasks/id

### 获取任务详情

#### 请求URL

https://xxx.com/api.php/v1/tasks/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 22,
  "project": 41,
  "parent": 0,
  "execution": 42,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "name": "多人任务",
  "type": "devel",
  "pri": 3,
  "estimate": 2,
  "consumed": 0,
  "left": 2,
  "deadline": "2021-12-23",
  "status": "wait",
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
  "openedDate": "2021-12-05T12:00:57Z",
  "assignedTo": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "assignedDate": "2021-12-05T12:00:57Z",
  "estStarted": "2021-12-05",
  "realStarted": null,
  "finishedBy": null,
  "finishedDate": null,
  "finishedList": "",
  "canceledBy": null,
  "canceledDate": null,
  "closedBy": null,
  "closedDate": null,
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": null,
  "lastEditedDate": null,
  "activatedDate": "",
  "deleted": false,
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "管理员",
  "children": [],
  "team": [
    {
      "id": 50,
      "root": 22,
      "type": "task",
      "account": "admin",
      "role": "",
      "limited": "no",
      "join": "2021-12-05",
      "days": 0,
      "hours": 0,
      "estimate": 1,
      "consumed": 0,
      "left": 1,
      "order": 0,
      "realname": "管理员",
      "avatar": "",
      "progress": 0
    },
    {
      "id": 51,
      "root": 22,
      "type": "task",
      "account": "productManager",
      "role": "",
      "limited": "no",
      "join": "2021-12-05",
      "days": 0,
      "hours": 0,
      "estimate": 1,
      "consumed": 0,
      "left": 1,
      "order": 1,
      "realname": "产品经理",
      "avatar": "",
      "progress": 0
    }
  ],
  "files": [],
  "needConfirm": false,
  "progress": 0,
  "storySpec": "",
  "storyVerify": "",
  "storyFiles": [],
  "executionName": "testt",
  "moduleTitle": "/",
  "actions": [
    {
      "id": 1253748,
      "objectType": "task",
      "objectID": 22,
      "product": ",4,",
      "project": 41,
      "execution": 42,
      "actor": "管理员",
      "action": "opened",
      "date": "2021-12-05 20:00:57",
      "comment": "",
      "extra": "",
      "read": "1",
      "history": [],
      "desc": "2021-12-05 20:00:57, 由 <strong>管理员</strong> 创建。\n"
    }
  ],
  "preAndNext": {
    "pre": "",
    "next": ""
  }
}
```

---

## 7. 修改任务

**Source**: https://www.zentao.net/book/api/718.html

#### 本篇目录

修改任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/tasks/id

### 修改任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| module | int | 否  | 所属模块 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "name": "testtt",
  "assignedTo": "admin",
  "type": "devel",
  "estStarted": "2021-12-01",
  "deadline": "2021-12-31"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 13,
  "project": 7,
  "parent": 0,
  "execution": 1,
  "module": 0,
  "design": 0,
  "story": 2,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "name": "ccc",
  "type": "devel",
  "pri": 1,
  "estimate": 10,
  "consumed": 0,
  "left": 10,
  "deadline": null,
  "status": "wait",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "新闻中心的开发",
  "version": 2,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "openedDate": "2021-04-28T05:16:15Z",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "2021-04-28T05:16:15Z",
  "estStarted": "",
  "realStarted": null,
  "finishedBy": null,
  "finishedDate": null,
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
  "lastEditedDate": "2021-12-05T12:57:10Z",
  "activatedDate": "",
  "deleted": false,
  "storyID": 2,
  "storyTitle": "新闻中心的设计和开发。",
  "latestStoryVersion": 1,
  "storyStatus": "active",
  "assignedToRealName": "开发甲",
  "children": [],
  "team": [],
  "files": [],
  "cases": {
    "3": "新闻中心的测试用例"
  },
  "needConfirm": false,
  "progress": 0
}
```

---

## 7. 开始任务

**Source**: https://www.zentao.net/book/api/967.html

#### 本篇目录

开始任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/start

### 开始任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/start

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| assignedTo | string | 否  | 指派给 |
| ---------- | ------ | --- | ------ |

#### 请求示例

```json
{
  "assignedTo": "test",
  "realStarted": "2022-12-02 11:04:59",
  "consumed": 2,
  "left": 2,
  "comment": "开始任务"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 2,
  "left": 2,
  "deadline": "2022-12-31",
  "status": "doing",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2022-12-02 13:08:49",
  "assignedTo": "test",
  "assignedDate": "2022-12-02 13:08:49",
  "estStarted": "2022-12-01",
  "realStarted": "2022-12-02 11:04:59",
  "finishedBy": "",
  "finishedDate": "",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": "",
  "closedBy": "",
  "closedDate": "",
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2022-12-02 14:07:21",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "林晨",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 50
}
```

---

## 7. 暂停任务

**Source**: https://www.zentao.net/book/api/968.html

#### 本篇目录

暂停任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/pause

### 暂停任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/pause

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| comment | string | 否  | 备注 |
| ------- | ------ | --- | ---- |

#### 请求示例

```json
{
  "comment": "暂停任务"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 2,
  "left": 2,
  "deadline": "2022-12-31",
  "status": "doing",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2022-12-02 13:08:49",
  "assignedTo": "test",
  "assignedDate": "2022-12-02 13:08:49",
  "estStarted": "2022-12-01",
  "realStarted": "2022-12-02 11:04:59",
  "finishedBy": "",
  "finishedDate": "",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": "",
  "closedBy": "",
  "closedDate": "",
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2022-12-02 14:07:21",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "林晨",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 50
}
```

---

## 7. 继续任务

**Source**: https://www.zentao.net/book/api/969.html

#### 本篇目录

继续任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/restart

### 继续任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/restart

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| assignedTo | string | 否  | 指派给 |
| ---------- | ------ | --- | ------ |

#### 请求示例

```json
{
  "assignedTo": "admin",
  "realStarted": "2022-12-02 14:04:59",
  "consumed": 3,
  "left": 3,
  "comment": "重新开始任务"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 3,
  "left": 3,
  "deadline": "2022-12-31",
  "status": "doing",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2022-12-02 13:08:49",
  "assignedTo": "admin",
  "assignedDate": "2022-12-02 15:37:21",
  "estStarted": "2022-12-01",
  "realStarted": "2022-12-02 14:04:59",
  "finishedBy": "",
  "finishedDate": "",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": "",
  "closedBy": "",
  "closedDate": "",
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2022-12-02 15:37:21",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "admin",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 50
}
```

---

## 7. 完成任务

**Source**: https://www.zentao.net/book/api/970.html

#### 本篇目录

完成任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/finish

### 完成任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/finish

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| assignedTo | string | 否  | 指派给，如果没填会使用任务当前的指派人 |
| ---------- | ------ | --- | -------------------------------------- |

#### 请求示例

```json
{
  "currentConsumed": 1,
  "assignedTo": "admin",
  "realStarted": "2022-12-02 14:04:59",
  "finishedDate": "2022-12-02 15:45:27",
  "comment": "完成任务"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 4,
  "left": 0,
  "deadline": "2022-12-31",
  "status": "done",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2022-12-02T05:08:49Z",
  "assignedTo": "admin",
  "assignedDate": "2022-12-02T07:55:26Z",
  "estStarted": "2022-12-01",
  "realStarted": "2022-12-02T06:04:59Z",
  "finishedBy": "admin",
  "finishedDate": "2022-12-02T07:45:27Z",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": null,
  "closedBy": "",
  "closedDate": null,
  "planDuration": 0,
  "realDuration": 1,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2022-12-02T07:55:26Z",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "admin",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 100
}
```

---

## 7. 关闭任务

**Source**: https://www.zentao.net/book/api/1200.html

#### 本篇目录

继续任务
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/close

### 继续任务

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/close

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| comment | string | 否  | 备注 |
| ------- | ------ | --- | ---- |

#### 请求示例

```json
{
  "comment": "关闭任务"
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 3,
  "left": 3,
  "deadline": "2024-12-31",
  "status": "closed",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2023-12-02 13:08:49",
  "assignedTo": "closed",
  "assignedDate": "2023-12-02 15:37:21",
  "estStarted": "2023-12-01",
  "realStarted": "2023-12-02 14:04:59",
  "finishedBy": "",
  "finishedDate": "",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": "",
  "closedBy": "admin",
  "closedDate": "2024-04-07 12:03:22",
  "planDuration": 0,
  "realDuration": 0,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2024-03-02 15:37:21",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "admin",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 50
}
```

---

## 7. 添加任务日志

**Source**: https://www.zentao.net/book/api/1198.html

#### 本篇目录

添加任务日志
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/tasks/id/estimate

###

### 添加任务日志

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/estimate

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

对于禅道开源版20.7（企业版10.6、旗舰版5.6、IPD版2.6）之前的版本，使用下面的请求体
| id | array | <br/> | 从0自增，表示记录几条日志，如3条日志则填入 [0,1,2] |
| --- | --- | --- | --- |
对于禅道开源版20.7（企业版10.6、旗舰版5.6、IPD版2.6）及之后的版本，使用下面的请求体
| date | <br/> | <br/> |
| --- | --- | --- |

#### 请求示例

对于禅道开源版20.7（企业版10.6、旗舰版5.6、IPD版2.6）之前的版本，使用下面的请求示例

```json
{
  "id": [0, 1, 2],
  "objectID": [2, 2, 2],
  "dates": ["2024-02-27", "2024-02-28", "2024-02-29"],
  "work": ["work1", "work2", "work3"],
  "consumed": [2, 2, 2],
  "left": [6, 4, 2],
  "objectType": ["task", "task", "task"]
}
```

对于禅道开源版20.7（企业版10.6、旗舰版5.6、IPD版2.6）
及之后
的版本，使用下面的请求示例

```json
{
  "date": ["2024-02-27", "2024-02-28", "2024-02-29"],
  "work": ["work1", "work2", "work3"],
  "consumed": [2, 2, 2],
  "left": [6, 4, 2]
}
```

#### 请求响应

| id  | int | 是  | 任务ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "project": 1,
  "parent": 0,
  "execution": 2,
  "module": 0,
  "design": 0,
  "story": 0,
  "storyVersion": 1,
  "designVersion": 0,
  "fromBug": 0,
  "feedback": 0,
  "fromIssue": 0,
  "name": "testtt",
  "type": "devel",
  "mode": "",
  "pri": 0,
  "estimate": 0,
  "consumed": 6,
  "left": 2,
  "deadline": "2024-04-31",
  "status": "doing",
  "subStatus": "",
  "color": "",
  "mailto": null,
  "desc": "",
  "version": 1,
  "openedBy": "admin",
  "openedDate": "2024-02-02T05:08:49Z",
  "assignedTo": "admin",
  "assignedDate": "2024-02-02T07:55:26Z",
  "estStarted": "2024-02-01",
  "realStarted": "2024-02-02T06:04:59Z",
  "finishedBy": "admin",
  "finishedDate": "2024-02-02T07:45:27Z",
  "finishedList": "",
  "canceledBy": "",
  "canceledDate": null,
  "closedBy": "",
  "closedDate": null,
  "planDuration": 0,
  "realDuration": 1,
  "closedReason": "",
  "lastEditedBy": "admin",
  "lastEditedDate": "2024-02-02T07:55:26Z",
  "activatedDate": "",
  "order": 0,
  "repo": 0,
  "mr": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "deleted": "0",
  "vision": "rnd",
  "storyID": null,
  "storyTitle": null,
  "latestStoryVersion": null,
  "storyStatus": null,
  "assignedToRealName": "admin",
  "children": [],
  "members": [],
  "team": [],
  "files": [],
  "needConfirm": false,
  "progress": 80
}
```

---

## 7. 获取任务日志

**Source**: https://www.zentao.net/book/api/1199.html

#### 本篇目录

获取任务日志列表
请求URL
请求头
请求响应
响应示例
GET
/tasks/id/estimate

### 获取任务日志列表

#### 请求URL

https://xxx.com/api.php/v1/tasks/id/estimate

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| effort | class | 是  | 日志列表 |
| ------ | ----- | --- | -------- |

#### 响应示例

```json
{
  "effort": {
    "9": {
      "id": 9,
      "objectType": "task",
      "objectID": 2,
      "product": ",10,",
      "project": 12,
      "execution": 13,
      "account": "admin",
      "work": "work3",
      "vision": "rnd",
      "date": "2024-02-29",
      "left": 2,
      "consumed": 2,
      "begin": "0000",
      "end": "0000",
      "extra": "",
      "order": 0,
      "deleted": "0"
    }
  }
}
```
