# ZenTao Feedbacks API


## 7. 创建反馈

**Source**: https://www.zentao.net/book/api/840.html

#### 本篇目录

创建反馈
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/feedbacks

### 创建反馈

#### 请求URL

https://xxx.com/api.php/v1/feedbacks

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

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 14,
  "product": 2,
  "module": 0,
  "title": "create test feedback",
  "type": "",
  "solution": "",
  "desc": "",
  "status": "wait",
  "subStatus": "",
  "public": "0",
  "notify": "0",
  "notifyEmail": "",
  "likes": "",
  "result": 0,
  "faq": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "openedDate": "2022-06-28T05:35:43Z",
  "reviewedBy": null,
  "reviewedDate": null,
  "processedBy": null,
  "processedDate": null,
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "editedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "editedDate": "2022-06-28T05:35:43Z",
  "assignedTo": null,
  "assignedDate": "2022-06-28T05:35:43Z",
  "feedbackBy": null,
  "mailto": [],
  "deleted": false,
  "likesCount": 0,
  "files": []
}
```

---

## 7. 指派反馈

**Source**: https://www.zentao.net/book/api/841.html

#### 本篇目录

指派反馈
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/feedbacks/id/assign

### 指派反馈

#### 请求URL

https://xxx.com/api.php/v1/feedbacks/id/assign

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| <br/> | <br/> |
| ----- | ----- |

#### 请求示例

```json
{
  "assignedTo": "admin",
  "comment": "yes"
}
```

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 2,
  "product": 2,
  "module": 0,
  "title": "test",
  "type": "",
  "solution": "",
  "desc": "edit test1",
  "status": "wait",
  "subStatus": "",
  "public": "1",
  "notify": "1",
  "notifyEmail": "",
  "likes": "",
  "result": 0,
  "faq": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "openedDate": "2022-06-10T00:56:02Z",
  "reviewedBy": "",
  "reviewedDate": "0000-00-00 00:00:00",
  "processedBy": "",
  "processedDate": "0000-00-00 00:00:00",
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "editedBy": "admin",
  "editedDate": "2022-06-28 11:55:08",
  "assignedTo": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "assignedDate": "2022-06-28T03:55:08Z",
  "feedbackBy": "",
  "mailto": [],
  "deleted": false,
  "likesCount": 0,
  "files": []
}
```

---

## 7. 关闭反馈

**Source**: https://www.zentao.net/book/api/842.html

#### 本篇目录

关闭反馈
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/feedbacks/id/close

### 关闭反馈

#### 请求URL

https://xxx.com/api.php/v1/feedbacks/id/close

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| <br/> | <br/> | <br/> |
| ----- | ----- | ----- |

#### 请求示例

```json
{
  "closedReason": "repeat"
}
```

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 2,
  "product": 2,
  "module": 0,
  "title": "test",
  "type": "",
  "solution": "",
  "desc": "edit test1",
  "status": "closed",
  "subStatus": "",
  "public": "1",
  "notify": "1",
  "notifyEmail": "",
  "likes": "",
  "result": 0,
  "faq": 0,
  "openedBy": "admin",
  "openedDate": "2022-06-10 08:56:02",
  "reviewedBy": "",
  "reviewedDate": "0000-00-00 00:00:00",
  "processedBy": "",
  "processedDate": "0000-00-00 00:00:00",
  "closedBy": "admin",
  "closedDate": "2022-06-28 13:15:42",
  "closedReason": "repeat",
  "editedBy": "admin",
  "editedDate": "2022-06-28 13:15:42",
  "assignedTo": "closed",
  "assignedDate": "2022-06-28 11:55:08",
  "feedbackBy": "",
  "mailto": "",
  "deleted": "0",
  "likesCount": 0,
  "files": []
}
```

---

## 7. 修改反馈

**Source**: https://www.zentao.net/book/api/844.html

#### 本篇目录

修改反馈
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/feedbacks/id

### 修改反馈

#### 请求URL

https://xxx.com/api.php/v1/feedbacks/id

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

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 2,
  "product": 2,
  "module": 0,
  "title": "test",
  "type": "",
  "solution": "",
  "desc": "edit test",
  "status": "wait",
  "subStatus": "",
  "public": "0",
  "notify": "1",
  "notifyEmail": "",
  "likes": "",
  "result": 0,
  "faq": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "openedDate": "2022-06-10T00:56:02Z",
  "reviewedBy": null,
  "reviewedDate": null,
  "processedBy": null,
  "processedDate": null,
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "editedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "editedDate": "2022-06-28T02:48:38Z",
  "assignedTo": "admin",
  "assignedDate": "2022-06-10 15:56:14",
  "feedbackBy": "",
  "mailto": [],
  "deleted": false,
  "likesCount": 0,
  "files": []
}
```

---

## 7. 获取反馈详情

**Source**: https://www.zentao.net/book/api/845.html

#### 本篇目录

获取反馈详情
请求URL
请求头
请求响应
响应示例
GET
/feedbacks/id

### 获取反馈详情

#### 请求URL

https://xxx.com/api.php/v1/feedbacks/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| 是  |
| --- |

#### 响应示例

```json
{
  "id": 4,
  "product": 2,
  "module": 0,
  "title": "一个反馈",
  "type": "",
  "solution": "",
  "desc": "",
  "status": "wait",
  "subStatus": "",
  "public": "0",
  "notify": "1",
  "notifyEmail": "",
  "likes": "",
  "result": 0,
  "faq": 0,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "admin"
  },
  "openedDate": "2022-06-10T03:18:52Z",
  "reviewedBy": "",
  "reviewedDate": "0000-00-00 00:00:00",
  "processedBy": "",
  "processedDate": "0000-00-00 00:00:00",
  "closedBy": null,
  "closedDate": null,
  "closedReason": "",
  "editedBy": "admin",
  "editedDate": "2022-06-10 11:18:52",
  "assignedTo": null,
  "assignedDate": "2022-06-10T03:18:52Z",
  "feedbackBy": "",
  "mailto": [],
  "deleted": false,
  "likesCount": 0,
  "files": [],
  "likeIcon": "thumbs-up",
  "publicStatus": "0",
  "productName": "产品X",
  "moduleName": "/",
  "resultType": "",
  "actions": [
    {
      "id": 163,
      "objectType": "feedback",
      "objectID": 4,
      "product": ",0,",
      "project": 0,
      "execution": 0,
      "actor": "admin",
      "action": "opened",
      "date": "2022-06-10 11:18:52",
      "comment": "",
      "extra": "",
      "read": "0",
      "vision": "rnd",
      "efforted": 0,
      "history": [],
      "desc": "2022-06-10 11:18:52, 由 <strong>admin</strong> 创建。\n"
    }
  ]
}
```

---

## 7. 获取反馈列表

**Source**: https://www.zentao.net/book/api/846.html

#### 本篇目录

获取反馈列表
请求URL
请求头
请求体
请求响应
响应示例
GET
/feedbacks

### 获取反馈列表

#### 请求URL

https://xxx.com/api.php/v1/feedbacks

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| <br/> | <br/> |
| ----- | ----- |

#### 请求响应

| <br/> | <br/> | <br/> | <br/> |
| ----- | ----- | ----- | ----- |

#### 响应示例

```json
{
  "page": 1,
  "total": 1,
  "limit": 20,
  "feedbacks": [
    {
      "id": 2,
      "product": 2,
      "module": 0,
      "title": "一个反馈",
      "type": "",
      "solution": "",
      "desc": "",
      "status": "wait",
      "subStatus": "",
      "public": "0",
      "notify": "1",
      "notifyEmail": "",
      "likes": "",
      "result": 0,
      "faq": 0,
      "openedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "admin"
      },
      "openedDate": "2022-06-10T00:56:02Z",
      "reviewedBy": null,
      "reviewedDate": null,
      "processedBy": null,
      "processedDate": null,
      "closedBy": null,
      "closedDate": null,
      "closedReason": "",
      "editedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "admin"
      },
      "editedDate": "2022-06-10T00:56:02Z",
      "assignedTo": null,
      "assignedDate": "2022-06-10 08:56:02",
      "feedbackBy": "",
      "mailto": [],
      "deleted": false,
      "dept": 0
    }
  ]
}
```
