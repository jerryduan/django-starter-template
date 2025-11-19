# Django Starter Template 项目介绍

本项目是一个用于快速构建基于 Django 与 Django REST Framework（DRF）的现代化 API 的起始模板，集成了认证、异步任务、自动化文档、结构化日志、速率限制与完整的开发文档，开箱即用并可按需扩展。

## 项目定位
- 面向后端 API 的工程化模板，聚焦“安全、可观测、可维护”
- 提供用户认证、任务队列、自动文档与统一日志的基础设施
- 适合从零开始的中小型服务或企业内部 API

## 技术栈
- 框架：`Django 5`、`Django REST Framework`
- 认证：`django-rest-knox`（Bearer Token）
- 任务队列：`Celery` + `Redis`，含周期任务与失败重试
- 文档：`drf-spectacular` 自动生成 OpenAPI 3 + Swagger UI
- 缓存：`django-redis`（默认 Redis）
- 日志与监控：`python-json-logger` 结构化日志；`Sentry`（非调试模式启用）
- 其他：`django-cors-headers`、`whitenoise`、`django-filter`、`django-extensions`
- 开发与测试：`Poetry` 管理依赖与脚本、`pytest` 测试、`MkDocs` 文档

## 目录结构速览
- `apps/users/` 用户域：自定义用户模型（邮箱登录）、视图与序列化器
- `apps/core/` 核心域：示例端点、日志中间件、任务示例
- `conf/` 框架层：`settings.py`、`urls.py`、`celery.py`、`wsgi/asgi`
- `scripts/` 开发脚本：启动服务、迁移、Celery、环境创建、数据填充
- `docs/` 项目文档：开发、结构、设置、认证、日志、任务、测试等
- `templates/` 模板：包含演示首页与错误页
- `.devcontainer/` VS Code Dev Container（PostgreSQL、Redis、容器化开发）
- 根目录：`pyproject.toml`、`README.md`、`mkdocs.yml`、`pytest.ini`、`.env.example`

详见文档 `docs/project_structure.md`。

## 关键特性
- 用户认证：基于 `Bearer` Token，登录速率限制与安全日志（`apps/users/views.py:27-43`）
- 自动文档：`DEBUG=True` 时提供 Swagger UI `GET /api/schema/swagger-ui/`（`conf/urls.py:39-44`）
- 结构化日志：含 `request_id`、响应时间、用户等上下文（`apps/core/middleware.py:19-43`；`conf/settings.py:230-327`）
- 异步任务：任务失败自动重试与周期任务（`apps/core/tasks.py:10-38`、`apps/core/tasks.py:40-68`）
- 速率限制：登录与匿名接口速率（`apps/users/throttles.py:29-37`；`apps/core/views.py:8-10,31`）
- 自定义用户：邮箱为唯一凭证（`apps/users/models.py:8-33`）

## 快速开始

### 方式一：VS Code Dev Container（推荐）
1. 安装：VS Code、Docker Desktop、Dev Containers 扩展
2. 打开项目后选择“Reopen in Container”
3. 创建超管：`python manage.py createsuperuser`
4. 启动服务：`python manage.py runserver`
5. 访问：`http://127.0.0.1:8000`

详细步骤见 `docs/index.md`。

### 方式二：本地运行（Poetry）
1. 准备 PostgreSQL 与 Redis（或使用 `.devcontainer/docker-compose.yml`）
2. 初始化环境文件：`poetry run create_dev_env`（生成 `.env`，含 `DEBUG/DATABASE_URL`）
3. 安装依赖：`poetry install`
4. 迁移数据库：`python manage.py migrate`
5. 创建超管：`python manage.py createsuperuser`
6. 启动服务：`python manage.py runserver`
7. 启动 Celery：`python manage.py worker`，周期任务：`python manage.py beat`

## 核心端点
- 管理后台：`/admin-panel/`（请自定义路径，`conf/urls.py:27`）
- 认证模块（`apps/users/urls.py:9-15`）：
  - `POST /auth/login/` 登录（返回 Token）
  - `POST /auth/logout/` 登出当前 Token
  - `POST /auth/logoutall/` 清除所有 Token
  - `GET/PUT/PATCH /auth/profile/` 当前用户信息
  - `POST /auth/create/` 创建用户（需认证）
- 核心模块（`apps/core/urls.py:7-11`）：
  - `GET /core/ping/` 健康检查
  - `GET /core/fire-task/` 触发示例 Celery 任务（仅用于演示，后续移除）
- 文档（调试模式）：`GET /api/schema/swagger-ui/`（`conf/urls.py:39-44`）

## 配置与环境变量
- 基本：`DEBUG`、`DJANGO_SECRET_KEY`、`ALLOWED_HOSTS`、`DATABASE_URL`
- 缓存与队列：`REDIS_URL`、`CELERY_BROKER_URL`、`CELERY_RESULT_BACKEND`
- CORS：`CORS_ALLOWED_ORIGINS`（生产）
- 监控：`SENTRY_DSN`（非调试模式启用）
- 邮件：`EMAIL_HOST/EMAIL_PORT/EMAIL_HOST_USER/EMAIL_HOST_PASSWORD`

详见 `conf/settings.py` 与文档 `docs/settings.md`。

## 日志与监控
- 结构化日志输出到 `logs/`：`app.log`、`info.log`、`error.log`、`security.log`
- 响应时间、请求 ID、客户端 IP、用户 ID 等均入日志（`apps/core/middleware.py:46-63`）
- 生产环境自动初始化 Sentry（`conf/settings.py:329-339`）

## 测试与质量
- 测试：`pytest`，示例测试见 `apps/users/tests/`、`apps/core/tests/`
- 代码质量：`flake8`、覆盖率 `pytest-cov`
- CI：GitHub Actions（`/.github/workflows/test.yml`）

## 常见下一步
- 替换 `pyproject.toml` 项目信息（`[tool.poetry]`）
- 自定义管理后台路径与关闭不需要的认证端点（`conf/urls.py:24-33`）
- 调整 DRF 速率限制与文档信息（`conf/settings.py:145-160`、`conf/settings.py:162-169`）
- 移除示例视图与任务（`apps/core/views.py:38-50`、`apps/core/tasks.py:40-68`）
- 配置生产环境的 CORS、Sentry 与静态资源

更多细节与操作指南请浏览 `docs/` 目录。