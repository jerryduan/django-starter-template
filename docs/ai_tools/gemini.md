# Gemini CLI Agent

本页为 Gemini CLI Agent 在 `django-starter-template` 项目中的使用提供具体指南与上下文。完整、最新的规则请参阅项目根目录的 `GEMINI.md`。

## 项目概览

本项目是一个用于快速开发的 Django REST Framework API 模板，预先配置了认证、后台任务、API 文档与结构化日志。

## 关键技术与约定

*   **框架**：Django 5.x
*   **API 框架**：Django REST Framework（DRF）
*   **依赖管理**：使用 [Poetry](https://python-poetry.org/)
    *   使用 `poetry run <command>` 执行项目脚本（如 `poetry run server`、`poetry run pytest`）
    *   依赖定义见 `pyproject.toml`，锁定文件 `poetry.lock`
*   **测试**：使用 [Pytest](https://docs.pytest.org/en/stable/)
    *   测试文件位于 `apps/<app_name>/tests/`
    *   运行测试：`poetry run test` 或 `poetry run pytest`
    *   覆盖率报告：`poetry run test-cov`
*   **API 文档**：使用 [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
    *   生成 OpenAPI 3 Schema
    *   Schema 多集中在各应用的 `schema.py`（如 `apps/users/schema.py`）
    *   视图上使用 `@extend_schema` 增强文档
*   **站点文档（MkDocs）**：基于 [MkDocs](https://www.mkdocs.org/) 与 Material 主题
    *   文档源文件位于 `docs/`
    *   站点配置见 `mkdocs.yml`
    *   调整文档时保持与现有页面风格一致
*   **环境变量**：使用 `django-environ`
    *   变量从 `.env` 加载，参考 `.env.example`
*   **异步任务**：使用 [Celery](https://docs.celeryq.dev/en/stable/) 与 Redis
    *   Worker：`poetry run worker`
    *   Beat：`poetry run beat`
*   **日志**：结构化 JSON 日志
    *   日志位于 `logs/`
    *   `RequestIDMiddleware` 提供请求追踪
*   **代码质量**：使用 [Flake8](https://flake8.pycqa.org/en/latest/)
    *   配置文件 `.flake8`
*   **开发环境**：为 VS Code Dev Containers 设计
    *   保证一致与可复现的环境

## Gemini 通用指引

*   **遵循现有代码风格**：修改/新增代码应匹配周边的格式、命名与架构模式
*   **确认依赖**：新增库前检查 `pyproject.toml` 与 `poetry.lock`
*   **优先使用现有方案**：如 API 文档用 `drf-spectacular`，后台任务用 Celery
*   **解释命令**：涉及修改文件系统或项目状态的命令应给出简要说明
*   **测试**：逻辑变更应补充/更新测试，使用 `poetry run test` 验证
*   **文档**：重大变更需更新 `docs/` 对应页面，保持风格一致
