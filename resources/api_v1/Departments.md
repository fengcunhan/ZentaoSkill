# ZenTao Departments API


## 7. 获取部门列表

**Source**: https://www.zentao.net/book/api/964.html

#### 本篇目录

获取部门列表
请求URL
请求头
请求响应
响应示例
GET
/departments

### 获取部门列表

#### 请求URL

https://xxx.com/api.php/v1/departments

#### 请求头

| Token | String | 是  | 访问凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| departments | array | 是  | 部门列表 |
| ----------- | ----- | --- | -------- |

#### 响应示例

```json
[
  {
    "id": 1,
    "name": "dept1",
    "parent": 0,
    "path": ",1,",
    "grade": 1,
    "order": 10,
    "position": "",
    "function": "",
    "manager": "",
    "managerName": ""
  },
  {
    "id": 2,
    "name": "dept2",
    "parent": 0,
    "path": ",2,",
    "grade": 1,
    "order": 20,
    "position": "",
    "function": "",
    "manager": "",
    "managerName": ""
  }
]
```

---

## 7. 获取部门详情

**Source**: https://www.zentao.net/book/api/965.html

#### 本篇目录

获取部门详情
请求URL
请求头
请求响应
响应示例
GET
/departments/id

### 获取部门详情

#### 请求URL

https://xxx.com/api.php/v1/departments/id

#### 请求头

| Token | String | 是  | 访问凭证Token |
| ----- | ------ | --- | ------------- |

#### 请求响应

| id  | int | 是  |
| --- | --- | --- |

#### 响应示例

```json
{
  "id": 1,
  "name": "dept1",
  "parent": 0,
  "path": ",1,",
  "grade": 1,
  "order": 10,
  "position": "",
  "function": "",
  "manager": ""
}
```
