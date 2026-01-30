# ZenTao Misc API


## 7. 创建计划

**Source**: https://www.zentao.net/book/api/681.html

#### 本篇目录

创建计划
请求URL
请求头
请求体
请求响应
响应示例
POST
/products/id/plans

### 创建计划

#### 请求URL

https://xxx.com/api.php/v1/products/id/plans

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "product": 4,
  "branch": 0,
  "parent": 0,
  "title": "主干计划",
  "desc": "",
  "begin": "2021-11-23",
  "end": "2021-11-29",
  "order": "",
  "deleted": false,
  "stories": [
    {
      "story": 12,
      "plan": "2",
      "order": 1,
      "id": 12,
      "parent": 0,
      "product": 4,
      "branch": 0,
      "module": 23,
      "source": "",
      "sourceNote": "",
      "fromBug": 0,
      "title": "主干需求",
      "keywords": "",
      "type": "story",
      "category": "feature",
      "pri": 0,
      "estimate": 0,
      "status": "active",
      "subStatus": "",
      "color": "",
      "stage": "planned",
      "stagedBy": "",
      "mailto": null,
      "openedBy": "admin",
      "openedDate": "2021-11-23 16:04:30",
      "assignedTo": "admin",
      "assignedDate": "2021-11-23 19:42:55",
      "lastEditedBy": "admin",
      "lastEditedDate": "2021-11-23 19:42:55",
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
  "bugs": [
    {
      "id": 5,
      "project": 0,
      "product": 4,
      "branch": 1,
      "module": 24,
      "execution": 0,
      "plan": 2,
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
      "steps": "<p>[步骤]</p><br /><p>[结果]</p><br /><p>[期望]</p><br />",
      "status": "active",
      "subStatus": "",
      "color": "",
      "confirmed": 0,
      "activatedCount": 0,
      "activatedDate": "0000-00-00 00:00:00",
      "mailto": "",
      "openedBy": "admin",
      "openedDate": "2021-11-29 13:02:34",
      "openedBuild": "trunk",
      "assignedTo": "",
      "assignedDate": "0000-00-00 00:00:00",
      "deadline": "2021-11-29",
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

## 7. 获取计划详情

**Source**: https://www.zentao.net/book/api/682.html

#### 本篇目录

获取计划详情
请求URL
请求头
请求响应
响应示例
GET
/productplans/id

### 获取计划详情

#### 请求URL

https://xxx.com/api.php/v1/productplans/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "product": 4,
  "branch": 0,
  "parent": 0,
  "title": "主干计划",
  "desc": "",
  "begin": "2021-11-23",
  "end": "2021-11-29",
  "order": "",
  "deleted": false,
  "stories": [
    {
      "story": 12,
      "plan": "2",
      "order": 1,
      "id": 12,
      "parent": 0,
      "product": 4,
      "branch": 0,
      "module": 23,
      "source": "",
      "sourceNote": "",
      "fromBug": 0,
      "title": "主干需求",
      "keywords": "",
      "type": "story",
      "category": "feature",
      "pri": 0,
      "estimate": 0,
      "status": "active",
      "subStatus": "",
      "color": "",
      "stage": "planned",
      "stagedBy": "",
      "mailto": null,
      "openedBy": "admin",
      "openedDate": "2021-11-23 16:04:30",
      "assignedTo": "admin",
      "assignedDate": "2021-11-23 19:42:55",
      "lastEditedBy": "admin",
      "lastEditedDate": "2021-11-23 19:42:55",
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
  "bugs": [
    {
      "id": 5,
      "project": 0,
      "product": 4,
      "branch": 1,
      "module": 24,
      "execution": 0,
      "plan": 2,
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
      "steps": "<p>[步骤]</p><br /><p>[结果]</p><br /><p>[期望]</p><br />",
      "status": "active",
      "subStatus": "",
      "color": "",
      "confirmed": 0,
      "activatedCount": 0,
      "activatedDate": "0000-00-00 00:00:00",
      "mailto": "",
      "openedBy": "admin",
      "openedDate": "2021-11-29 13:02:34",
      "openedBuild": "trunk",
      "assignedTo": "",
      "assignedDate": "0000-00-00 00:00:00",
      "deadline": "2021-11-29",
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

## 7. 修改计划

**Source**: https://www.zentao.net/book/api/683.html

#### 本篇目录

修改计划
请求URL
请求头
请求体
请求响应
响应示例
PUT
/productplans/id

### 修改计划

#### 请求URL

https://xxx.com/api.php/v1/productplans/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求响应

| id  | int | 是  | 计划ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 2,
  "product": 4,
  "branch": 0,
  "parent": 0,
  "title": "主干计划",
  "desc": "",
  "begin": "2021-11-23",
  "end": "2021-11-29",
  "order": "",
  "deleted": false,
  "stories": [
    {
      "story": 12,
      "plan": "2",
      "order": 1,
      "id": 12,
      "parent": 0,
      "product": 4,
      "branch": 0,
      "module": 23,
      "source": "",
      "sourceNote": "",
      "fromBug": 0,
      "title": "主干需求",
      "keywords": "",
      "type": "story",
      "category": "feature",
      "pri": 0,
      "estimate": 0,
      "status": "active",
      "subStatus": "",
      "color": "",
      "stage": "planned",
      "stagedBy": "",
      "mailto": null,
      "openedBy": "admin",
      "openedDate": "2021-11-23 16:04:30",
      "assignedTo": "admin",
      "assignedDate": "2021-11-23 19:42:55",
      "lastEditedBy": "admin",
      "lastEditedDate": "2021-11-23 19:42:55",
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
  "bugs": [
    {
      "id": 5,
      "project": 0,
      "product": 4,
      "branch": 1,
      "module": 24,
      "execution": 0,
      "plan": 2,
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
      "steps": "<p>[步骤]</p><br /><p>[结果]</p><br /><p>[期望]</p><br />",
      "status": "active",
      "subStatus": "",
      "color": "",
      "confirmed": 0,
      "activatedCount": 0,
      "activatedDate": "0000-00-00 00:00:00",
      "mailto": "",
      "openedBy": "admin",
      "openedDate": "2021-11-29 13:02:34",
      "openedBuild": "trunk",
      "assignedTo": "",
      "assignedDate": "0000-00-00 00:00:00",
      "deadline": "2021-11-29",
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
