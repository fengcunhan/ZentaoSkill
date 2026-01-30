# ZenTao Users API


## 7. 获取我的个人信息

**Source**: https://www.zentao.net/book/api/665.html

#### 本篇目录

获取我的个人信息
请求URL
请求头
请求响应
响应示例
GET
/user

### 获取我的个人信息

#### 请求URL

https://xxx.com/api.php/v1/user

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| profile | object | 是  |
| ------- | ------ | --- |

#### 响应示例

```json
{
  "profile": {
    "id": 1,
    "company": 0,
    "type": "inside",
    "dept": 0,
    "account": "admin",
    "role": {
      "code": "",
      "name": ""
    },
    "realname": "admin",
    "nickname": "",
    "commiter": "",
    "avatar": "",
    "birthday": null,
    "gender": "f",
    "email": "",
    "skype": "",
    "qq": "",
    "mobile": "",
    "phone": "",
    "weixin": "",
    "dingding": "",
    "slack": "",
    "whatsapp": "",
    "address": "",
    "zipcode": "",
    "nature": "",
    "analysis": "",
    "strategy": "",
    "join": null,
    "visits": 10,
    "ip": "127.0.0.1",
    "last": "2021-11-28T16:31:40Z",
    "fails": 0,
    "locked": null,
    "ranzhi": "",
    "score": 0,
    "scoreLevel": 0,
    "deleted": "0",
    "admin": true
  }
}
```

---

## 7. 获取用户列表

**Source**: https://www.zentao.net/book/api/666.html

#### 本篇目录

获取用户列表
请求URL
请求头
请求参数
请求响应
响应示例
GET
/users

### 获取用户列表

#### 请求URL

https://xxx.com/api.php/v1/users

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求参数

| browse | string | 否  | 人员类型，默认为 inside（内部人员），可选 inside outside（外部人员），如果填入了其他的内容（比如空）查询所有用户 |
| ------ | ------ | --- | ---------------------------------------------------------------------------------------------------------------- |

#### 请求响应

| page | int | 是  | 当前页数 |
| ---- | --- | --- | -------- |

#### 响应示例

```json
{
  "page": 1,
  "total": 3,
  "limit": 20,
  "users": [
    {
      "id": 3,
      "dept": 6,
      "account": "projectManager",
      "realname": "项目经理",
      "role": "pm",
      "email": ""
    },
    {
      "id": 2,
      "dept": 5,
      "account": "productManager",
      "realname": "产品经理",
      "role": "po",
      "email": ""
    },
    {
      "id": 1,
      "dept": 0,
      "account": "admin",
      "realname": "admin",
      "role": "",
      "email": ""
    }
  ]
}
```

---

## 7. 获取用户信息

**Source**: https://www.zentao.net/book/api/667.html

#### 本篇目录

获取用户信息
请求URL
请求头
请求响应
响应示例
GET
/users/id

### 获取用户信息

#### 请求URL

https://xxx.com/api.php/v1/users/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 用户编号 |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 2,
  "company": 0,
  "type": "inside",
  "dept": 5,
  "account": "productManager",
  "role": "po",
  "realname": "产品经理",
  "nickname": "",
  "commiter": "",
  "avatar": "",
  "birthday": "0000-00-00",
  "gender": "m",
  "email": "",
  "skype": "",
  "qq": "",
  "mobile": "",
  "phone": "",
  "weixin": "",
  "dingding": "",
  "slack": "",
  "whatsapp": "",
  "address": "",
  "zipcode": "",
  "nature": "",
  "analysis": "",
  "strategy": "",
  "join": "0000-00-00",
  "visits": 3,
  "ip": "192.168.0.8",
  "last": "2012-06-05 11:14:43",
  "fails": 0,
  "locked": "0000-00-00 00:00:00",
  "ranzhi": "",
  "score": 0,
  "scoreLevel": 0,
  "deleted": "0"
}
```

---

## 7. 修改用户信息

**Source**: https://www.zentao.net/book/api/668.html

#### 本篇目录

修改用户信息
请求URL
请求头
请求体
请求示例
请求响应
响应示例
PUT
/users/id

### 修改用户信息

#### 请求URL

https://xxx.com/api.php/v1/users/id

#### 请求头

| Token | String | 是  | 认证凭证 |
| ----- | ------ | --- | -------- |

#### 请求体

| dept | int | 否  | 所属部门 |
| ---- | --- | --- | -------- |

#### 请求示例

```json
{
  "realname": "管理员"
}
```

#### 请求响应

| id  | int | 是  | 用户编号 |
| --- | --- | --- | -------- |

#### 响应示例

```json
{
  "id": 2,
  "company": 0,
  "type": "inside",
  "dept": 5,
  "account": "productManager",
  "role": "po",
  "realname": "产品经理",
  "nickname": "",
  "commiter": "",
  "avatar": "",
  "birthday": "0000-00-00",
  "gender": "m",
  "email": "",
  "skype": "",
  "qq": "",
  "mobile": "",
  "phone": "",
  "weixin": "",
  "dingding": "",
  "slack": "",
  "whatsapp": "",
  "address": "",
  "zipcode": "",
  "nature": "",
  "analysis": "",
  "strategy": "",
  "join": "0000-00-00",
  "visits": 3,
  "ip": "192.168.0.8",
  "last": "2012-06-05 11:14:43",
  "fails": 0,
  "locked": "0000-00-00 00:00:00",
  "ranzhi": "",
  "score": 0,
  "scoreLevel": 0,
  "deleted": "0"
}
```

---

## 7. 创建用户

**Source**: https://www.zentao.net/book/api/838.html

#### 本篇目录

创建用户
请求URL
请求头
请求体
请求响应
响应示例
POST
/users

### 创建用户

#### 请求URL

https://xxx.com/api.php/v1/users

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| <br/> | string | 是  | 账号 |
| ----- | ------ | --- | ---- |

请求示例

```json
{ "account": "usertest", "password": "123qwe!@#", "realname": "测试用户" }
```

#### 请求响应

| id  | int | 是  | 用户id |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 8,
  "company": 0,
  "type": "inside",
  "dept": 0,
  "account": "usertest",
  "role": "",
  "realname": "测试用户",
  "pinyin": "",
  "nickname": "",
  "commiter": "",
  "avatar": "",
  "birthday": "0000-00-00",
  "gender": "f",
  "email": "",
  "skype": "",
  "qq": "",
  "mobile": "",
  "phone": "",
  "weixin": "",
  "dingding": "",
  "slack": "",
  "whatsapp": "",
  "address": "",
  "zipcode": "",
  "nature": "",
  "analysis": "",
  "strategy": "",
  "join": "0000-00-00",
  "visits": 0,
  "visions": "rnd",
  "ip": "",
  "last": "1970-01-01T00:00:00Z",
  "fails": 0,
  "locked": null,
  "feedback": "0",
  "ranzhi": "",
  "ldap": "",
  "score": 0,
  "scoreLevel": 0,
  "deleted": "0",
  "clientStatus": "offline",
  "clientLang": "zh-cn"
}
```
