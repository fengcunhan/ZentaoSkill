# ZenTao Releases API


## 7. 获取产品发布列表

**Source**: https://www.zentao.net/book/api/689.html

#### 本篇目录

获取产品发布列表
请求URL
请求头
请求响应
响应示例
GET
/products/id/releases

### 获取产品发布列表

#### 请求URL

https://xxx.com/api.php/v1/products/id/releases

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| total | int | 是  | 发布总数 |
| ----- | --- | --- | -------- |

#### 响应示例

```json
{
  "total": 1,
  "releases": [
    {
      "id": 1,
      "project": 41,
      "product": 4,
      "branch": 0,
      "build": 3,
      "name": "发布test",
      "marker": "0",
      "date": "2021-12-02",
      "stories": "",
      "bugs": "",
      "leftBugs": "",
      "desc": "",
      "mailto": "",
      "notify": null,
      "status": "normal",
      "subStatus": "",
      "deleted": false,
      "productName": "多分支产品",
      "buildID": 3,
      "buildName": "test",
      "projectName": "测试"
    }
  ]
}
```

---

## 7. 获取项目发布列表

**Source**: https://www.zentao.net/book/api/690.html

#### 本篇目录

获取项目发布列表
请求URL
请求头
请求响应
响应示例
GET
/projects/id/releases

### 获取项目发布列表

#### 请求URL

https://xxx.com/api.php/v1/projects/id/releases

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| total | int | 是  | 发布总数 |
| ----- | --- | --- | -------- |

#### 响应示例

```json
{
  "total": 1,
  "releases": [
    {
      "id": 1,
      "project": 41,
      "product": 4,
      "branch": 0,
      "build": 3,
      "name": "发布test",
      "marker": "0",
      "date": "2021-12-02",
      "stories": "",
      "bugs": "",
      "leftBugs": "",
      "desc": "",
      "mailto": "",
      "notify": null,
      "status": "normal",
      "subStatus": "",
      "deleted": false,
      "productName": "多分支产品",
      "buildID": 3,
      "buildName": "test",
      "projectName": "测试"
    }
  ]
}
```
