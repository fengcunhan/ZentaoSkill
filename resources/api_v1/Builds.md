# ZenTao Builds API


## 7. 创建版本

**Source**: https://www.zentao.net/book/api/706.html

#### 本篇目录

创建版本
请求URL
请求头
请求体
请求示例
请求响应
响应示例
POST
/projects/id/builds

### 创建版本

#### 请求URL

https://xxx.com/api.php/v1/projects/id/builds

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求体

| execution | int | 是  | 所属执行 |
| --------- | --- | --- | -------- |

#### 请求示例

```json
{
  "name": "test",
  "product": 4,
  "date": "2021-01-01",
  "execution": 42,
  "builder": "admin"
}
```

#### 请求响应

| id  | int | 是  | 版本ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 3,
  "project": 41,
  "product": 4,
  "branch": 0,
  "execution": 42,
  "name": "test",
  "scmPath": "",
  "filePath": "",
  "date": "2021-01-01",
  "stories": "",
  "bugs": "",
  "builder": "admin",
  "desc": "",
  "deleted": "0",
  "executionName": "testt",
  "productName": "多分支产品",
  "productType": "branch",
  "files": []
}
```

---

## 7. 获取版本详情

**Source**: https://www.zentao.net/book/api/707.html

#### 本篇目录

获取版本详情
请求URL
请求头
请求响应
响应示例
GET
/builds/id

### 获取版本详情

#### 请求URL

https://xxx.com/api.php/v1/builds/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 版本ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 3,
  "project": 41,
  "product": 4,
  "branch": 0,
  "execution": 42,
  "name": "test",
  "scmPath": "",
  "filePath": "",
  "date": "2021-01-01",
  "stories": "",
  "bugs": "",
  "builder": "admin",
  "desc": "",
  "deleted": "0",
  "executionName": "testt",
  "productName": "多分支产品",
  "productType": "branch",
  "files": []
}
```

---

## 7. 修改版本

**Source**: https://www.zentao.net/book/api/708.html

#### 本篇目录

修改版本
请求URL
请求头
请求响应
响应示例
PUT
/builds/id

### 修改版本

#### 请求URL

https://xxx.com/api.php/v1/builds/id

#### 请求头

| Token | String | 是  | 认证凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  | 版本ID |
| --- | --- | --- | ------ |

#### 响应示例

```json
{
  "id": 3,
  "project": 41,
  "product": 4,
  "branch": 0,
  "execution": 42,
  "name": "test",
  "scmPath": "",
  "filePath": "",
  "date": "2021-01-01",
  "stories": "",
  "bugs": "",
  "builder": "admin",
  "desc": "",
  "deleted": "0",
  "executionName": "testt",
  "productName": "多分支产品",
  "productType": "branch",
  "files": []
}
```
