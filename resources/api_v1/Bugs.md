# ZenTao Bugs API


## 7. 创建Bug

**Source**: https://www.zentao.net/book/api/721.html

#### 本篇目录

创建Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/products/id/bugs

### 创建Bug

#### 请求URL

https://xxx.com/api.php/v1/products/id/bugs

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "title": "Bug2",
  "severity": 1,
  "pri": 1,
  "steps": "",
  "type": "codeerror",
  "openedBuild": ["trunk"]
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": [],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 获取Bug详情

**Source**: https://www.zentao.net/book/api/722.html

#### 本篇目录

获取Bug详情
请求URL
请求头
请求响应
响应示例
GET
/bugs/id

### 获取Bug详情

#### 请求URL

https://xxx.com/api.php/v1/bugs/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": [],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 修改Bug

**Source**: https://www.zentao.net/book/api/723.html

#### 本篇目录

修改Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/bugs/id

### 修改Bug

#### 请求URL

https://xxx.com/api.php/v1/bugs/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| branch | int | 否  | 所属分支 |
| ------ | --- | --- | -------- |

#### 请求示例

```json
{
  "title": "Bug2",
  "severity": 1,
  "pri": 1,
  "steps": "",
  "type": "codeerror",
  "openedBuild": ["trunk"]
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": [],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 确认Bug

**Source**: https://www.zentao.net/book/api/1120.html

#### 本篇目录

确认Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/bugs/id/confirm

### 确认Bug

#### 请求URL

https://xxx.com/api.php/v1/bugs/id/confirm

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
  "mailto": ["lihua"],
  "pri": 1,
  "type": "codeerror",
  "comment": "this is a comment"
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": ["lihua"],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 关闭Bug

**Source**: https://www.zentao.net/book/api/1121.html

#### 本篇目录

关闭Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/bugs/id/close

### 关闭Bug

#### 请求URL

https://xxx.com/api.php/v1/bugs/id/close

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| comment | string | 否  | 备注 |
| ------- | ------ | --- | ---- |

#### 请求示例

```json
{
  "comment": "this is a comment"
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": ["lihua"],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 激活Bug

**Source**: https://www.zentao.net/book/api/1142.html

#### 本篇目录

激活Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/bugs/id/active

### 激活Bug

#### 请求URL

https://xxx.com/api.php/v1/bugs/id/active

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| assignedTo | string | 否  | 指派给 |
| ---------- | ------ | --- | ------ |

#### 请求示例

```json
{
  "assignedTo": "dev1",
  "openedBuild": ["trunk"],
  "comment": "active bug"
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 1,
  "project": 7,
  "product": 1,
  "branch": 0,
  "module": 0,
  "execution": 1,
  "plan": 0,
  "story": 1,
  "storyVersion": 1,
  "task": 1,
  "toTask": 0,
  "toStory": 0,
  "title": "aaa",
  "keywords": "",
  "severity": 3,
  "pri": 1,
  "type": "codeerror",
  "os": "",
  "browser": "",
  "hardware": "",
  "found": "",
  "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
  "status": "active",
  "subStatus": "",
  "color": "",
  "confirmed": 0,
  "activatedCount": 0,
  "activatedDate": "1969-12-31T16:00:00Z",
  "feedbackBy": "",
  "notifyEmail": "",
  "mailto": ["lihua"],
  "openedBy": {
    "id": 7,
    "account": "tester1",
    "avatar": "",
    "realname": "测试甲"
  },
  "openedDate": "2012-06-05T02:56:11Z",
  "openedBuild": "trunk",
  "assignedTo": {
    "id": 4,
    "account": "dev1",
    "avatar": "",
    "realname": "开发甲"
  },
  "assignedDate": "1969-12-31T16:00:00Z",
  "deadline": null,
  "resolvedBy": null,
  "resolution": "",
  "resolvedBuild": "",
  "resolvedDate": null,
  "closedBy": null,
  "closedDate": "1969-12-31T16:00:00Z",
  "duplicateBug": 0,
  "linkBug": "",
  "case": 0,
  "caseVersion": 1,
  "result": 0,
  "repo": 0,
  "entry": "",
  "lines": "",
  "v1": "",
  "v2": "",
  "repoType": "",
  "testtask": 0,
  "lastEditedBy": {
    "id": 1,
    "account": "admin",
    "avatar": "",
    "realname": "管理员"
  },
  "lastEditedDate": "2021-12-05T14:53:35Z",
  "deleted": false,
  "executionName": "企业网站第一期",
  "storyTitle": "首页设计和开发",
  "storyStatus": "active",
  "latestStoryVersion": 2,
  "taskName": null,
  "planName": null,
  "projectName": "企业管理系统",
  "toCases": [],
  "files": []
}
```

---

## 7. 解决Bug

**Source**: https://www.zentao.net/book/api/1181.html

#### 本篇目录

解决Bug
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/bugs/id/resolve

### 解决Bug

#### 请求URL

https://xxx.com/api.php/v1/bugs/id/resolve

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| resolution | string | 是  |
| ---------- | ------ | --- |

#### 请求示例

```json
{
  "resolution": "duplicate",
  "duplicateBug": 5,
  "resolvedBuild": "trunk",
  "resolvedDate": "2023-07-02 20:10:45",
  "assignedTo": "admin",
  "comment": "fix bug comment"
}
```

#### 请求响应

| id  | int | 是  | Bug ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
    "id": 1,
    "project": 7,
    "product": 1,
    "branch": 0,
    "module": 0,
    "execution": 1,
    "plan": 0,
    "story": 1,
    "storyVersion": 1,
    "task": 1,
    "toTask": 0,
    "toStory": 0,
    "title": "aaa",
    "keywords": "",
    "severity": 3,
    "pri": 1,
    "type": "codeerror",
    "os": "",
    "browser": "",
    "hardware": "",
    "found": "",
    "steps": "<p>[步骤]进入首页</p>\r\n<p>[结果]出现乱码&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n<p>[期望]正常显示</p>",
    "status": "resolved",
    "subStatus": "",
    "color": "",
    "confirmed": 0,
    "activatedCount": 0,
    "activatedDate": "1969-12-31T16:00:00Z",
    "feedbackBy": "",
    "notifyEmail": "",
    "mailto": ["lihua"],
    "openedBy": {
        "id": 7,
        "account": "tester1",
        "avatar": "",
        "realname": "测试甲"
    },
    "openedDate": "2012-06-05T02:56:11Z",
    "openedBuild": "trunk",
    "assignedTo": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "admin"
    },
    "assignedDate": "2023-07-02 20:10:45",
    "deadline": null,
    "resolvedBy": admin,
    "resolution": "duplicate",
    "resolvedBuild": "trunk",
    "resolvedDate":2023-07-02 20:10:45,
    "closedBy": null,
    "closedDate": null,
    "duplicateBug": 0,
    "linkBug": "",
    "case": 0,
    "caseVersion": 1,
    "result": 0,
    "repo": 0,
    "entry": "",
    "lines": "",
    "v1": "",
    "v2": "",
    "repoType": "",
    "testtask": 0,
    "lastEditedBy": {
        "id": 1,
        "account": "admin",
        "avatar": "",
        "realname": "管理员"
    },
    "lastEditedDate": "2021-12-05T14:53:35Z",
    "deleted": false,
    "executionName": "企业网站第一期",
    "storyTitle": "首页设计和开发",
    "storyStatus": "active",
    "latestStoryVersion": 2,
    "taskName": null,
    "planName": null,
    "projectName": "企业管理系统",
    "toCases": [],
    "files": []
}
```
