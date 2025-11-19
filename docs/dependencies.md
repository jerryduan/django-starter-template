# 项目依赖

## 概览

本项目使用 [Poetry](https://python-poetry.org/) 管理依赖与虚拟环境。所有依赖在 `pyproject.toml` 中定义，分为生产依赖与开发依赖。

## 生产依赖

以下为生产环境所需的主要依赖：

*   **`python`**：Python 版本约束 `^3.13`
*   **`django`**：Web 框架 `^5.1.2`
*   **`django-environ`**：环境变量管理 `^0.12.0`
*   **`django-cors-headers`**：CORS 处理 `^4.5.0`
*   **`djangorestframework`**：Web API 工具包 `^3.15.2`
*   **`psycopg2`**：PostgreSQL 适配器 `^2.9.10`
*   **`whitenoise`**：生产静态文件服务 `^6.7.0`
*   **`gunicorn`**：WSGI 服务器 `^23.0.0`
*   **`django-rest-knox`**：基于 Token 的认证 `^5.0.2`
*   **`redis`**：Redis 客户端 `^6.0.0`
*   **`celery`**：分布式任务队列 `^5.4.0`
*   **`django-celery-beat`**：周期任务调度器 `^2.7.0`
*   **`django-celery-results`**：Celery 结果存储 `^2.5.1`
*   **`sentry-sdk`**：Sentry Python SDK（Django 集成）`^2.17.0`
*   **`django-redis`**：Redis 缓存后端 `^6.0.0`
*   **`drf-spectacular`**：OpenAPI 3 文档生成 `^0.28.0`
*   **`faker`**：生成测试/开发用假数据 `^37.1.0`
*   **`django-seed`**：批量填充数据 `^0.3.1`
*   **`django-extensions`**：Django 扩展集 `^4.1`
*   **`django-filter`**：查询过滤 `^25.1`
*   **`python-json-logger`**：JSON 日志格式化 `^3.3.0`


## 开发依赖

- **django-debug-toolbar**：^5.0.0
- **pytest**：^8.3.3
- **pytest-django**：^4.9.0
- **ipykernel**：^6.29.5
- **pytest-mock**：^3.14.0
- **pytest-cov**：^6.0.0
- **mkdocs**：^1.6.0
- **mkdocs-material**：^9.5.26
