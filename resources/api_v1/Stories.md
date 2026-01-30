# ZenTao Stories API


## 7. 获取产品需求列表

**Source**: https://www.zentao.net/book/api/691.html

#### 本篇目录

获取产品需求列表
请求URL
请求头
请求参数
响应示例
GET
/products/id/stories

### 获取产品需求列表

#### 请求URL

https://xxx.com/api.php/v1/products/id/stories

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| page | String | 否  | 当前页数 |
| ---- | ------ | --- | -------- |

请求响应
| page | int | 是 | 当前页面 |
| --- | --- | --- | --- |

#### 响应示例

"page": 1,
"total": 1,
"limit": 20,
"stories": [
{
"id": 7,
"parent": 0,
"product": 1,
"branch": 0,
"module": 7,
"plan": "1",
"source": "po",
"sourceNote": "",
"fromBug": 0,
"title": "关于我们的设计和开发",
"keywords": "",
"type": "story",
"category": "feature",
"pri": 1,
"estimate": 1,
"status": "draft",
"subStatus": "",
"color": "",
"stage": "planned",
"stagedBy": "",
"mailto": "",
"openedBy": "productManager",
"openedDate": "2012-06-05T02:24:19Z",
"assignedTo": "productManager",
"assignedDate": "2012-06-05T02:24:19Z",
"lastEditedBy": "",
"lastEditedDate": null,
"reviewedBy": "",
"reviewedDate": null,
"closedBy": "",
"closedDate": null,
"closedReason": "",
"toBug": 0,
"childStories": "",
"linkStories": "",
"duplicateStory": 0,
"version": 1,
"URChanged": "0",
"deleted": false,
"planTitle": "1.0版本 "
}
]
}

---

## 7. 获取项目需求列表

**Source**: https://www.zentao.net/book/api/692.html

#### 本篇目录

获取项目需求列表
请求URL
请求头
请求响应
响应示例
GET
/projects/id/stories

### 获取项目需求列表

#### 请求URL

https://xxx.com/api.php/v1/projects/id/stories

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| page | int | 是  | 当前页面 |
| ---- | --- | --- | -------- |

#### 响应示例

"page": 1,
"total": 1,
"limit": 20,
"stories": [
{
"id": 7,
"parent": 0,
"product": 1,
"branch": 0,
"module": 7,
"plan": "1",
"source": "po",
"sourceNote": "",
"fromBug": 0,
"title": "关于我们的设计和开发",
"keywords": "",
"type": "story",
"category": "feature",
"pri": 1,
"estimate": 1,
"status": "draft",
"subStatus": "",
"color": "",
"stage": "planned",
"stagedBy": "",
"mailto": "",
"openedBy": "productManager",
"openedDate": "2012-06-05T02:24:19Z",
"assignedTo": "productManager",
"assignedDate": "2012-06-05T02:24:19Z",
"lastEditedBy": "",
"lastEditedDate": null,
"reviewedBy": "",
"reviewedDate": null,
"closedBy": "",
"closedDate": null,
"closedReason": "",
"toBug": 0,
"childStories": "",
"linkStories": "",
"duplicateStory": 0,
"version": 1,
"URChanged": "0",
"deleted": false,
"planTitle": "1.0版本 "
}
]
}

---

## 34. 获取执行需求列表

**Error fetching content**: HTTPSConnectionPool(host='www.zentao.net', port=443): Read timed out. (read timeout=10)

---

## 7. 创建需求

**Source**: https://www.zentao.net/book/api/694.html

#### 本篇目录

创建需求
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/stories

### 创建需求

#### 请求URL

https://xxx.com/api.php/v1/stories

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| title | string | 是  | 需求标题 |
| ----- | ------ | --- | -------- |

#### 请求示例

```json
{
  "title": "测试需求",
  "spec": "测试",
  "product": 1,
  "pri": 1,
  "category": "feature"
}
```

#### 请求响应

| id  | int | 是  | 需求ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 14,
  "parent": 0,
  "product": 1,
  "branch": 0,
  "module": 0,
  "plan": "",
  "source": "",
  "sourceNote": "",
  "fromBug": 0,
  "title": "测试需求",
  "keywords": "",
  "type": "story",
  "category": "feature",
  "pri": 1,
  "estimate": 0,
  "status": "active",
  "subStatus": "",
  "color": "",
  "stage": "wait",
  "stagedBy": "",
  "mailto": null,
  "openedBy": "admin",
  "openedDate": "2021-11-29T01:18:02Z",
  "assignedTo": "",
  "assignedDate": null,
  "lastEditedBy": "",
  "lastEditedDate": null,
  "reviewedBy": "",
  "reviewedDate": null,
  "closedBy": "",
  "closedDate": null,
  "closedReason": "",
  "toBug": 0,
  "childStories": "",
  "linkStories": "",
  "duplicateStory": 0,
  "version": 1,
  "URChanged": "0",
  "deleted": false,
  "spec": "测试",
  "verify": "",
  "executions": [],
  "tasks": [],
  "stages": [],
  "children": []
}
```

---

## 7. 获取需求详情

**Source**: https://www.zentao.net/book/api/695.html

#### 本篇目录

获取需求详情
请求URL
请求头
请求响应
响应示例
GET
/stories/id

### 获取需求详情

#### 请求URL

https://xxx.com/api.php/v1/stories/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 需求ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 14,
  "parent": 0,
  "product": 1,
  "branch": 0,
  "module": 0,
  "plan": "",
  "source": "",
  "sourceNote": "",
  "fromBug": 0,
  "title": "测试需求",
  "keywords": "",
  "type": "story",
  "category": "feature",
  "pri": 1,
  "estimate": 0,
  "status": "active",
  "subStatus": "",
  "color": "",
  "stage": "wait",
  "stagedBy": "",
  "mailto": null,
  "openedBy": "admin",
  "openedDate": "2021-11-29T01:18:02Z",
  "assignedTo": "",
  "assignedDate": null,
  "lastEditedBy": "",
  "lastEditedDate": null,
  "reviewedBy": "",
  "reviewedDate": null,
  "closedBy": "",
  "closedDate": null,
  "closedReason": "",
  "toBug": 0,
  "childStories": "",
  "linkStories": "",
  "duplicateStory": 0,
  "version": 1,
  "URChanged": "0",
  "deleted": false,
  "spec": "测试",
  "verify": "",
  "executions": [],
  "tasks": [],
  "stages": [],
  "children": []
}
```

---

## 7. 变更需求

**Source**: https://www.zentao.net/book/api/696.html

#### 本篇目录

变更需求
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/stories/id/change

### 变更需求

#### 请求URL

https://xxx.com/api.php/v1/stories/id/change

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| title | string | 否  | 需求标题 |
| ----- | ------ | --- | -------- |

#### 请求示例

```json
{
  "spec": "变更描述"
}
```

#### 请求响应

| id  | int | 是  | 需求ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "parent": 0,
  "product": 1,
  "branch": 0,
  "module": 1,
  "plan": "1",
  "source": "po",
  "sourceNote": "",
  "fromBug": 0,
  "title": "首页设计和开发",
  "keywords": "",
  "type": "story",
  "category": "feature",
  "pri": 1,
  "estimate": 1,
  "status": "active",
  "subStatus": "",
  "color": "",
  "stage": "developing",
  "stagedBy": "",
  "mailto": "",
  "openedBy": "productManager",
  "openedDate": "2012-06-05T02:09:49Z",
  "assignedTo": "productManager",
  "assignedDate": null,
  "lastEditedBy": "admin",
  "lastEditedDate": "2021-11-29T01:43:18Z",
  "reviewedBy": "",
  "reviewedDate": null,
  "closedBy": "",
  "closedDate": null,
  "closedReason": "",
  "toBug": 0,
  "childStories": "",
  "linkStories": "",
  "duplicateStory": 0,
  "version": 2,
  "URChanged": "0",
  "deleted": "0",
  "spec": "变更描述",
  "verify": "开发并通过验收<br />",
  "executions": {
    "1": {
      "project": 1,
      "name": "企业网站第一期",
      "status": "doing"
    }
  },
  "tasks": {
    "1": [
      {
        "id": 11,
        "name": "首页页面的开发",
        "assignedTo": "dev1",
        "execution": 1,
        "status": "doing",
        "consumed": 0,
        "left": 8,
        "type": "devel"
      },
      {
        "id": 10,
        "name": "首页页面的设计",
        "assignedTo": "dev1",
        "execution": 1,
        "status": "done",
        "consumed": 8,
        "left": 0,
        "type": "design"
      }
    ]
  },
  "stages": [],
  "planTitle": {
    "1": "1.0版本"
  },
  "children": []
}
```

---

## 7. 修改需求其他字段

**Source**: https://www.zentao.net/book/api/697.html

#### 本篇目录

修改需求其他字段
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/stories/id

### 修改需求其他字段

#### 请求URL

https://xxx.com/api.php/v1/stories/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| module | int | 否  | 所属模块 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "category": "other"
}
```

#### 请求响应

| id  | int | 是  | 需求ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 14,
  "parent": 0,
  "product": 1,
  "branch": 0,
  "module": 0,
  "plan": "",
  "source": "",
  "sourceNote": "",
  "fromBug": 0,
  "title": "测试需求",
  "keywords": "",
  "type": "story",
  "category": "feature",
  "pri": 1,
  "estimate": 0,
  "status": "active",
  "subStatus": "",
  "color": "",
  "stage": "wait",
  "stagedBy": "",
  "mailto": null,
  "openedBy": "admin",
  "openedDate": "2021-11-29T01:18:02Z",
  "assignedTo": "",
  "assignedDate": null,
  "lastEditedBy": "",
  "lastEditedDate": null,
  "reviewedBy": "",
  "reviewedDate": null,
  "closedBy": "",
  "closedDate": null,
  "closedReason": "",
  "toBug": 0,
  "childStories": "",
  "linkStories": "",
  "duplicateStory": 0,
  "version": 1,
  "URChanged": "0",
  "deleted": false,
  "spec": "测试",
  "verify": "",
  "executions": [],
  "tasks": [],
  "stages": [],
  "children": []
}
```

---

## 7. 关闭需求

**Source**: https://www.zentao.net/book/api/1060.html

#### 本篇目录

关闭需求
请求URL
请求头
请求体
请求示例
响应示例
POST
/stories/id/close

### 关闭需求

#### 请求URL

https://xxx.com/api.php/v1/stories/id/close

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

####

#### 请求体

| closedReason | string | 是  | 关闭原因（done 已完成 | duplicate 重复 | postponed 延期 | willnotdo 不做 | cancel 已取消 | bydesign 设计如此） |
| ------------ | ------ | --- | --------------------- | -------------- | -------------- | -------------- | ------------- | ------------------- |

#### 请求示例

```json
{
  "closedReason": "done",
  "comment": "close the story"
}
```

请求响应
| id | int | 是 | 需求ID |
| --- | --- | --- | --- |

#### 响应示例

```json
{
  "id": 1,
  "vision": "rnd",
  "parent": 0,
  "product": 1,
  "branch": 0,
  "module": 0,
  "plan": "",
  "source": "",
  "sourceNote": "",
  "fromBug": 0,
  "feedback": 2,
  "title": "222",
  "keywords": "",
  "type": "story",
  "category": "feature",
  "pri": 3,
  "estimate": 0,
  "status": "closed",
  "subStatus": "",
  "color": "",
  "stage": "closed",
  "stagedBy": "",
  "mailto": null,
  "lib": 0,
  "fromStory": 0,
  "fromVersion": 1,
  "openedBy": {
    "id": 1,
    "account": "admin",
    "avatar": null,
    "realname": "admin"
  },
  "openedDate": "2023-08-15T09:37:49Z",
  "assignedTo": null,
  "assignedDate": "2023-08-18T01:30:43Z",
  "approvedDate": null,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": null,
    "realname": "admin"
  },
  "lastEditedDate": "2023-08-18T01:30:43Z",
  "changedBy": "",
  "changedDate": null,
  "reviewedBy": null,
  "reviewedDate": null,
  "closedBy": {
    "id": 1,
    "account": "admin",
    "avatar": null,
    "realname": "admin"
  },
  "closedDate": "2023-08-18T01:30:43Z",
  "closedReason": "duplicate",
  "activatedDate": null,
  "toBug": 0,
  "childStories": "",
  "linkStories": "",
  "linkRequirements": "",
  "twins": "",
  "duplicateStory": 2,
  "version": 1,
  "storyChanged": "0",
  "feedbackBy": "",
  "notifyEmail": "",
  "BSA": "",
  "duration": "",
  "demand": 0,
  "submitedBy": "",
  "roadmap": "",
  "URChanged": "0",
  "deleted": false,
  "spec": "",
  "verify": "",
  "files": [],
  "executions": [],
  "tasks": [],
  "stages": [],
  "extraStories": {
    "2": "222"
  },
  "children": [],
  "feedbackTitle": "222"
}
```
