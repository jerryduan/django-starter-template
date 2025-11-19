# 项目设置

## 概览

本文档全面介绍 `conf/settings.py` 中的项目配置。理解这些设置有助于按需定制与正确部署应用。内容按逻辑分区组织，便于查阅。

## 环境变量

项目使用 `django-environ` 读取位于项目根目录的 `.env` 文件，以便将敏感信息与环境配置从版本库中隔离。

**示例代码：**

```python
import environ

env = environ.Env()
root_path = environ.Path(__file__) - 2
env.read_env(str(root_path.path(".env")))
```

**说明：**

*   `env = environ.Env()`：初始化环境读取器，支持类型转换。
*   `root_path`：用于解析项目内相对路径，定位到 `settings.py` 的上两级。
*   `env.read_env()`：读取根目录 `.env` 变量。

## 基础配置

以下为应用核心行为相关的基础设置：

*   `ROOT_URLCONF`：根 URL 配置模块。默认 `conf.urls`。
*   `WSGI_APPLICATION`：WSGI 入口。默认 `conf.wsgi.application`。
*   `DEBUG`：调试模式。默认 `False`；生产务必关闭以保障安全与性能。

## 时间与语言

These settings control the localization and time zone behavior of the Django application:

*   `LANGUAGE_CODE`：语言代码，默认 `en-us`。
*   `TIME_ZONE`：时区，默认 `UTC`。
*   `USE_I18N`：国际化开关，默认 `True`。
*   `USE_TZ`：时区支持，默认 `True`（数据库存 UTC，展示按时区转换）。

## 安全与用户

This section covers critical security configurations and user model settings, essential for protecting your application and managing user accounts:

*   `SECRET_KEY`：密钥，从 `DJANGO_SECRET_KEY` 环境变量读取，严禁泄露或硬编码。

    ```python
    SECRET_KEY = env("DJANGO_SECRET_KEY")
    ```

*   `ALLOWED_HOSTS`：允许的域名列表。默认 `[*]`，生产环境需明确域名。

    ```python
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
    ```

*   `AUTH_USER_MODEL`：自定义用户模型，默认 `users.CustomUser`（邮箱登录）。
*   `MIN_PASSWORD_LENGTH`：密码最小长度，默认 `8`。
*   `PASSWORD_HASHERS`：密码哈希算法列表，启用多种现代安全算法。
*   `AUTH_PASSWORD_VALIDATORS`：密码校验器集合，可按需加强策略。

### 安全头部

These settings configure various HTTP security headers to protect against common web vulnerabilities:

*   `SECURE_BROWSER_XSS_FILTER`：开启浏览器 XSS 保护。
*   `SECURE_CONTENT_TYPE_NOSNIFF`：禁止 MIME 嗅探。
*   `X_FRAME_OPTIONS`：点击劫持防护，默认 `DENY`。
*   `CSRF_COOKIE_SECURE`：仅 HTTPS 发送 CSRF Cookie（生产应开启）。
*   `SESSION_COOKIE_SECURE`：仅 HTTPS 发送会话 Cookie（生产应开启）。

## 数据库

Database connection settings are managed through the `DATABASE_URL` environment variable, which `django-environ` parses to configure the database connection.

**示例代码：**

```python
DJANGO_DATABASE_URL = env.db("DATABASE_URL")
DATABASES = {"default": DJANGO_DATABASE_URL}
```

**说明：**

*   `DJANGO_DATABASE_URL`：数据库连接字符串，从 `DATABASE_URL` 加载。
*   `DATABASES`：数据库配置字典，`default` 为主库。
*   `DEFAULT_AUTO_FIELD`：默认主键类型，使用 64 位 `BigAutoField`。

## 应用与中间件

This section details the configuration of installed Django applications and middleware, which are crucial for defining the project's functionalities and request-response processing flow:

*   `INSTALLED_APPS`：启用的 Django 应用列表（内置、第三方与本地应用）。
*   `MIDDLEWARE`：请求/响应全局处理链，顺序十分重要（含安全、中间件、CORS、认证、自定义 `RequestIDMiddleware` 等）。

## 模板

These settings configure Django's template engine, which is responsible for rendering HTML and other content:

*   `BACKEND`：模板引擎，默认 `DjangoTemplates`。
*   `DIRS`：模板搜索路径，默认 `[root_path("templates")]`。
*   `APP_DIRS`：开启应用内 `templates/` 搜索，默认 `True`。
*   `OPTIONS`：上下文处理器与内置过滤器等配置。

## REST Framework

This section details the settings for Django REST Framework (DRF) and related tools for API development, authentication, and schema generation.

### 基于 Token 的认证

Configuration for `django-rest-knox`, the token-based authentication system used for secure API access:

*   `SECURE_HASH_ALGORITHM`：Token 哈希算法，默认 `hashlib.sha512`。
*   `AUTH_TOKEN_CHARACTER_LENGTH`：令牌长度，默认 `64`。
*   `TOKEN_TTL`：令牌有效期，默认 `10 小时`。
*   `USER_SERIALIZER`：用户序列化器，默认 `apps.users.serializers.UserProfileSerializer`。
*   `TOKEN_LIMIT_PER_USER`：每用户令牌数量限制，默认不限制。
*   `AUTO_REFRESH`：是否自动刷新令牌，默认 `False`。
*   `AUTO_REFRESH_MAX_TTL`：自动刷新后的最大 TTL，默认 `None`。
*   `MIN_REFRESH_INTERVAL`：两次刷新最小间隔（秒），默认 `60`。
*   `AUTH_HEADER_PREFIX`：认证头前缀，默认 `Bearer`。
*   `TOKEN_MODEL`：Knox 令牌模型，默认 `knox.AuthToken`。

### DRF 通用设置

Core settings for Django REST Framework, influencing how APIs behave, including authentication, filtering, and rendering:

*   `DEFAULT_AUTHENTICATION_CLASSES`：默认认证方式；`DEBUG` 模式下附带会话与基础认证。
*   `DEFAULT_FILTER_BACKENDS`：默认过滤、搜索与排序后端。
*   `DEFAULT_RENDERER_CLASSES`：默认渲染器；`DEBUG` 模式下启用可浏览 API。
*   `DEFAULT_SCHEMA_CLASS`：OpenAPI Schema 生成类。
*   `DEFAULT_THROTTLE_RATES`：速率限制配置。

### OpenAPI 文档生成
Settings for `drf-spectacular`, which generates OpenAPI 3 documentation for your API:

*   `TITLE`：文档标题。
*   `DESCRIPTION`：文档简介。
*   `VERSION`：版本号。
*   `SERVE_INCLUDE_SCHEMA`：是否暴露原始 Schema 端点。

### CORS 设置

Settings related to Cross-Origin Resource Sharing (CORS), managed by `django-cors-headers`:

*   `CORS_ALLOW_ALL_ORIGINS`：是否允许所有来源；生产应设为 `False`。
*   `CORS_ALLOWED_ORIGINS`：允许的来源列表，生产环境需明确配置。

## 缓存

These settings configure the caching mechanism, primarily utilizing Redis for efficient data storage and retrieval:

*   `CACHES`：缓存后端配置，默认使用 Redis。
*   `LOCATION`：Redis 连接 URL。
*   `OPTIONS`：Redis 客户端选项。
*   `USER_AGENTS_CACHE`：UA 缓存别名。

## Celery

These settings configure Celery, the distributed task queue used for handling asynchronous tasks and periodic jobs:

*   `CELERY_BROKER_URL`：消息代理 URL（默认 Redis）。
*   `CELERY_RESULT_BACKEND`：结果存储后端（默认 Django DB）。
*   `CELERY_BEAT_SCHEDULER`：周期任务调度器，支持在后台管理配置。
*   `CELERY_ACCEPT_CONTENT`：接受的内容类型，默认仅 JSON。
*   `CELERY_TASK_SERIALIZER`：任务序列化方式，默认 JSON。
*   `CELERY_RESULT_SERIALIZER`：结果序列化方式，默认 JSON。
*   `CELERY_TIMEZONE`：任务调度时区。
*   `CELERY_RESULT_EXTENDED`：扩展结果存储，默认开启。

## 邮件

These settings configure the email backend, enabling the application to send emails for various purposes (e.g., user registration, password resets):

*   `EMAIL_HOST`：SMTP 服务器地址，默认 `smtp.gmail.com`。
*   `EMAIL_USE_TLS`：是否启用 TLS，默认 `True`。
*   `EMAIL_PORT`：SMTP 端口，默认 `587`。
*   `EMAIL_HOST_USER`：SMTP 用户名。
*   `EMAIL_HOST_PASSWORD`：SMTP 密码或专用密钥。

## Sentry 与日志

While the logging system has its own dedicated documentation page ([Logging System](logging.md)), this section briefly covers settings related to error tracking with Sentry and general logging configurations:

*   `IGNORABLE_404_URLS`：忽略的 404 路径模式，减少噪声。
*   `LOGGING`：日志系统配置，详见 [日志系统](logging.md)。
*   `sentry_sdk.init()`：生产环境初始化 Sentry 用于错误与性能监控。

## 静态与媒体文件

These settings govern how static files (CSS, JavaScript, images) and user-uploaded media files are handled and served by the Django application:

*   `STORAGES`：默认文件存储与静态文件存储后端配置（生产启用压缩与指纹）。
*   `STATIC_URL`：静态文件 URL 前缀，默认 `/static/`。
*   `STATICFILES_DIRS`：额外静态目录，默认 `[root_path("static")]`。
*   `STATIC_ROOT`：`collectstatic` 收集的静态输出目录。
*   `MEDIA_URL`: The URL prefix that handles media files served from `MEDIA_ROOT`. **Default:** `/media/`. This is used for user-uploaded content.
*   `MEDIA_ROOT`: The absolute path to the directory where user-uploaded media files are stored. **Default:** A `media_root` directory within the project root. **This directory should be configured for serving by your web server.**
*   `ADMIN_MEDIA_PREFIX`: The URL prefix for Django admin's static media files. **Default:** `/static/admin/`.

## Django Debug Toolbar and Django Extensions

These development-centric tools are conditionally enabled only when Django's `DEBUG` mode is active, providing valuable insights and utilities during development:

*   `debug_toolbar`: Integrates the Django Debug Toolbar, which provides a customizable debug panel for inspecting various aspects of your Django application (e.g., SQL queries, request/response headers, templates). **Default:** Automatically added to `INSTALLED_APPS` and `MIDDLEWARE` if `DEBUG` is `True`.
*   `INTERNAL_IPS`: A list of IP addresses that are considered "internal" for the Django Debug Toolbar. Requests originating from these IP addresses will display the debug toolbar. **Default:** `["127.0.0.1"]`.
*   `django_extensions`: Provides a collection of custom extensions for Django, including a variety of useful management commands (e.g., `runserver_plus`, `shell_plus`). **Default:** Automatically added to `INSTALLED_APPS` if `DEBUG` is `True`.

These settings are dynamically included in `INSTALLED_APPS` and `MIDDLEWARE` when `DEBUG` is `True`, ensuring they are only active in development environments.