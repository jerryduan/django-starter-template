# 速率限制（Rate Limiting）

速率限制用于控制用户或 IP 在一定时间窗口内的请求次数，有助于防止滥用、暴力破解，并保障资源的公平使用与服务稳定性。

## 为什么需要速率限制？

*   **安全**：抵御登录暴力破解、DoS、过度爬取。
*   **性能**：避免单个用户或恶意行为造成过载。
*   **公平使用**：防止资源被个别用户垄断。

## 实现方式

项目使用 DRF 内置的节流机制与自定义节流类实现速率限制。

### 1. 默认速率

全局速率在 `conf/settings.py` 的 `REST_FRAMEWORK` 中定义，按不同 scope 生效：

```python
# Example from conf/settings.py
REST_FRAMEWORK = {
    # ... other settings
    "DEFAULT_THROTTLE_RATES": {
        "user": "1000/day",
        "anon": "100/day",
        "user_login": "5/minute",
    },
}
```

*   `user`：认证用户，默认 `1000/day`
*   `anon`：匿名用户，默认 `100/day`
*   `user_login`：登录尝试，默认 `5/minute`

### 2. 自定义节流类

针对登录尝试等场景，使用自定义节流类（`apps/users/throttles.py`）实现更细粒度的限流标识与策略。

```python
# Example from apps/users/throttles.py
from rest_framework.throttling import SimpleRateThrottle

class UserLoginRateThrottle(SimpleRateThrottle):
    scope = "user_login"

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            ident = self.get_ident(request) # Uses IP for anonymous users
        else:
            ident = request.user.pk # Uses user ID for authenticated users

        return self.cache_format % {"scope": self.scope, "ident": ident}
```

该节流类确保：

*   匿名用户按 IP 限流
*   已认证用户按用户 ID 限流

### 3. 在视图中应用节流

通过 `throttle_classes` 将节流策略应用到 DRF 视图。

**Example (from `apps/users/views.py` for `LoginView` and `UserProfileView`):**

```python
# For LoginView
from rest_framework.throttling import AnonRateThrottle # Or other built-in throttles
from .throttles import UserLoginRateThrottle

class LoginView(KnoxLoginView):
    # ...
    throttle_classes = [UserLoginRateThrottle]

# For UserProfileView and CreateUserView
from rest_framework import throttling

class UserProfileView(generics.RetrieveUpdateAPIView):
    # ...
    throttle_classes = [throttling.UserRateThrottle]

class CreateUserView(generics.CreateAPIView):
    # ...
    throttle_classes = [throttling.UserRateThrottle]
```

*   `UserLoginRateThrottle`：用于 `LoginView` 控制登录尝试频率。
*   `throttling.UserRateThrottle`：用于认证用户的通用速率（`UserProfileView`、`CreateUserView`）。

## 配置方法

在 `conf/settings.py` 的 `DEFAULT_THROTTLE_RATES` 中修改限流策略即可。

例如，将匿名用户限流改为每小时 50 次：

```python
# In conf/settings.py
REST_FRAMEWORK = {
    # ...
    "DEFAULT_THROTTLE_RATES": {
        "user": "1000/day",
        "anon": "50/hour", # Changed from 100/day
        "user_login": "5/minute",
    },
}
```

You can also create new custom throttle classes in `apps/users/throttles.py` (or a similar location) and apply them to specific views as needed.
