# 认证系统

## 概览

本节介绍模板中的认证系统，包括核心认证端点、安全设置与基于 Token 的认证机制。

## 认证相关设置

`conf/settings.py` 中与认证与用户管理相关的设置：

*   `AUTH_USER_MODEL`：自定义用户模型，默认 `users.CustomUser`（支持扩展与邮箱登录）。

*   `MIN_PASSWORD_LENGTH`：密码最小长度，默认 `8`。

*   `PASSWORD_HASHERS`：密码哈希算法列表，默认启用多种现代安全算法。

*   `AUTH_PASSWORD_VALIDATORS`：密码校验器集合，可按需加强策略。

### 基于 Token 的认证

模板使用 `django-rest-knox` 提供安全的 Token 认证。以下 `REST_KNOX` 设置控制其行为：

*   `SECURE_HASH_ALGORITHM`：令牌哈希算法，默认 `hashlib.sha512`。
*   `AUTH_TOKEN_CHARACTER_LENGTH`：令牌长度，默认 `64`。
*   `TOKEN_TTL`：令牌有效期，默认 `10 小时`。
*   `USER_SERIALIZER`：用户序列化器，默认 `apps.users.serializers.UserProfileSerializer`。
*   `TOKEN_LIMIT_PER_USER`：每用户令牌数量限制，默认不限制。
*   `AUTO_REFRESH`：是否自动刷新令牌，默认 `False`。
*   `AUTO_REFRESH_MAX_TTL`：自动刷新最大 TTL，默认 `None`。
*   `MIN_REFRESH_INTERVAL`：刷新间隔（秒），默认 `60`。
*   `AUTH_HEADER_PREFIX`：认证头前缀，默认 `Bearer`。
*   `TOKEN_MODEL`：Knox 令牌模型，默认 `knox.AuthToken`。

### DRF 设置

DRF 的认证与速率限制用于管理访问与防止滥用：

*   `DEFAULT_AUTHENTICATION_CLASSES`：默认认证方式；`DEBUG` 模式下附带会话与基础认证。

*   `DEFAULT_THROTTLE_RATES`：速率限制（可调整）：
    *   `user: "1000/day"`（认证用户）
    *   `anon: "100/day"`（未认证用户）
    *   `user_login: "5/minute"`（登录尝试专用）

These rates can be adjusted in `conf/settings.py` to suit your application's specific needs and security requirements.

## 认证端点

### 创建用户

用于注册新用户。

**请求：**

*   **Method:** `POST`
*   **URL:** `/auth/create/`
*   **Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "complexpassword123",
        "password2": "complexpassword123"
    }
    ```
    *   `email`: The user's unique email address.
    *   `password`: The user's chosen password.
    *   `password2`: Confirmation of the user's chosen password (must match `password`).

**响应：**

*   **成功（201 Created）：**
    ```json
    {
        "email": "user@example.com"
    }
    ```
    *   返回新创建用户的邮箱。

*   **错误（400 Bad Request）：**
    *   **密码不一致：**
        ```json
        {
            "password": [
                "Passwords do not match."
            ]
        }
        ```
    *   **邮箱已注册：**
        ```json
        {
            "email": [
                "This email is already registered."
            ]
        }
        ```
    *   **密码不合法（过短、常见等）：**
        ```json
        {
            "password": [
                "This password is too short. It must contain at least 8 characters."
            ]
        }
        ```
*   **错误（401 Unauthorized）：**
    *   This error typically occurs if authentication credentials are required for this endpoint (though usually not for user creation).
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```

### 登录

认证用户并签发认证令牌。

**请求：**

*   **Method:** `POST`
*   **URL:** `/auth/login/`
*   **Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "complexpassword123"
    }
    ```
    *   `email`: The user's registered email address.
    *   `password`: The user's password.

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "expiry": "2025-07-09T12:00:00Z",
        "token": "your-auth-token",
        "user": {
            "email": "user@example.com",
            "first_name": "",
            "last_name": ""
        }
    }
    ```
    *   `expiry`：令牌过期时间戳。
    *   `token`：后续请求使用的认证令牌。
    *   `user`：用户基本信息。

*   **错误（400 Bad Request）：**
    *   **凭据无效：**
        ```json
        {
            "detail": "Unable to log in with provided credentials."
        }
        ```
    *   **缺少字段：**
        ```json
        {
            "email": [
                "This field is required."
            ],
            "password": [
                "This field is required."
            ]
        }
        ```

### 登出

使当前认证用户的令牌失效以登出。

**请求：**

*   **Method:** `POST`
*   **URL:** `/auth/logout/`
*   **Authentication:** Token required.

**响应：**

*   **成功（204 No Content）：**
    *   The response will have an empty body, indicating successful token invalidation.

*   **错误（401 Unauthorized）：**
    *   Occurs if no authentication credentials are provided or if the token is invalid.
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```

### 全部登出
使当前认证用户的所有令牌失效，退出全部设备。

**请求：**

*   **Method:** `POST`
*   **URL:** `/auth/logoutall/`
*   **Authentication:** Token required.

**响应：**

*   **成功（204 No Content）：**
    *   The response will have an empty body, indicating that all tokens for the user have been invalidated.

*   **错误（401 Unauthorized）：**
    *   Occurs if no authentication credentials are provided or if the token is invalid.
    ```json
    {
        "detail": "Authentication credentials were not provided."
    }
    ```

### 用户资料

允许认证用户获取与更新个人资料。

#### 获取用户资料

获取当前认证用户的资料。

**请求：**

*   **Method:** `GET`
*   **URL:** `/auth/profile/`
*   **Authentication:** Token required.

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }
    ```
    *   返回用户邮箱、名与姓。

*   **错误（401 Unauthorized）：**
    *   Occurs if no authentication credentials are provided or if the token is invalid.
    ```json
    {
    "detail": "Authentication credentials were not provided."
}
    ```

#### 更新用户资料（PUT）

整体验证并更新用户资料，需提供所有字段。

**请求：**

*   **Method:** `PUT`
*   **URL:** `/auth/profile/`
*   **Authentication:** Token required.
*   **Body:**
    ```json
    {
        "first_name": "Jane",
        "last_name": "Doe"
    }
    ```
    *   `first_name`: The user's first name.
    *   `last_name`: The user's last name.

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "email": "user@example.com",
        "first_name": "Jane",
        "last_name": "Doe"
    }
    ```
    *   返回更新后的资料。

*   **错误（400 Bad Request）：**
    *   Occurs if the provided data is invalid (e.g., password validation errors if password fields were included).
    ```json
    {
        "password": [
            "Password must be at least 8 characters long."
        ]
    }
    ```

*   **错误（401 Unauthorized）：**
    *   Occurs if no authentication credentials are provided or if the token is invalid.
    ```json
    {
    "detail": "Authentication credentials were not provided."
}
    ```

#### 局部更新用户资料（PATCH）

局部更新当前用户资料，仅提供需变更字段。

**请求：**

*   **Method:** `PATCH`
*   **URL:** `/auth/profile/`
*   **Authentication:** Token required.
*   **Body:**
    ```json
    {
        "first_name": "Jane"
    }
    ```
    *   `first_name`: The user's first name (optional).
    *   `last_name`: The user's last name (optional).

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "email": "user@example.com",
        "first_name": "Jane",
        "last_name": "Doe"
    }
    ```
    *   Returns the partially updated user profile.

*   **错误（401 Unauthorized）：**
    *   Occurs if no authentication credentials are provided or if the token is invalid.
    ```json
    {
    "detail": "Authentication credentials were not provided."
}
    ```