# ZenTao Authentication API


## 7. 获取Token

**Source**: https://www.zentao.net/book/api/664.html

#### 本篇目录

获取Token
请求URL
请求体
请求示例
请求响应
响应示例
POST
/tokens

### 获取Token

#### 请求URL

https://xxx.com/api.php/v1/tokens

#### 请求体

| account | string | 是  | 登录名 |
| ------- | ------ | --- | ------ |

#### 请求示例

```json
{ "account": "admin", "password": "123456" }
```

#### 请求响应

| token | string | 否  |
| ----- | ------ | --- |

#### 响应示例

```json
{
  "token": "cuejkiesahl9k1j8be5bv5lndo"
}
```
