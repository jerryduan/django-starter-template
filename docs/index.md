<h1 align="center">欢迎使用 Django Starter Template！</h1>

<p align="center">
  <img src="assets/logo.png" alt="Django Starter Template Logo" width="150"/>
</p>

<p align="center">
  <strong>一个用于基于 Django 与 DRF 构建新 API 的全面起始模板。</strong>
</p>

## 概览

本文档为 Django Starter Template 提供完整指南，帮助你在 Django 与 Django REST Framework 上构建现代化 API。内容涵盖环境搭建、开发流程到认证、异步任务与自动化文档等高级特性。

## 快速开始

推荐使用 VS Code 的 Dev Container 功能进行启动。

### 先决条件

使用 Dev Container 前，请确保已安装：

*   [Visual Studio Code](https://code.visualstudio.com/)
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### 安装步骤

按以下步骤通过 Dev Container 配置开发环境：

1.  **使用 GitHub 模板：** 在 [Django Starter Template 仓库](https://github.com/wilfredinni/django-starter-template) 点击绿色的 `Use this template` 按钮创建你的仓库。

2.  **在 VS Code 打开：** 将仓库克隆到本地并在 VS Code 中打开项目目录。

3.  **查看安装指引：** 在 VS Code 侧边栏打开 **`Todo Tree`**，按照清单完成初始设置。

4.  **在容器中重新打开：** VS Code 会提示“Reopen in Container”。点击后将自动构建并启动开发环境，配置 Redis、Celery、PostgreSQL，安装依赖并执行数据库迁移。

5.  **创建超管：** 容器准备完成后，运行 `python manage.py createsuperuser` 创建管理员账户。

6.  **启动服务：** 运行 `python manage.py runserver` 启动开发服务器。

此时 API 可在 `http://127.0.0.1:8000` 访问。

## 关键特性

模板内置丰富特性，加速你的 API 开发：

*   **用户认证：** 通过 `django-rest-knox` 实现安全的 Token 认证，覆盖用户管理与访问控制。
*   **后台任务：** 使用 `Celery` + `Redis` 处理异步任务，避免长耗时操作阻塞请求。
*   **API 文档：** 借助 `drf-spectacular` 自动生成 OpenAPI 3 Schema，可通过 Swagger UI 交互浏览。
*   **集中日志：** 结构化 JSON 日志，便于监控与排查。
*   **自定义用户模型：** 使用邮箱作为登录凭据，灵活且现代。
*   **AI 工具：** 集成多个开发助理的提示与指南（Copilot、Gemini、Roo Code/Cline）。
*   **完善文档：** 覆盖全部功能与实践，帮助你高效上手与扩展。

---

## 浏览文档

使用左侧导航，快速了解并深入使用本模板：

*   **[开发流程](development.md)：** 了解开发命令、如何运行测试以及脚本使用。
*   **[项目结构](project_structure.md)：** 全局目录结构与组织方式。
*   **[项目设置](settings.md)：** 配置项说明与环境差异化配置。
*   **[依赖说明](dependencies.md)：** 项目依赖与用途清单。
*   **[认证系统](authentication.md)：** 用户管理与 API 端点详解。
*   **[核心应用](core_endpoints.md)：** `apps/core` 的核心功能与关键端点。
*   **[日志系统](logging.md)：** 结构化日志与监控调试方法。
*   **[Celery 任务](tasks.md)：** 创建、管理与监控异步任务。
*   **[速率限制](rate_limiting.md)：** 防止滥用与保障公平使用的限流策略。
*   **[数据库灌数据](database_seeding.md)：** 在开发与测试阶段快速填充数据。
*   **[测试](testing.md)：** 编写与运行测试，确保质量与可靠性。
*   **[环境配置](environment_setup.md)：** 搭建开发环境的详细指南。
*   **[AI 工具](ai_tools)：** 使用 Copilot、Gemini CLI、Roo Code/Cline 提升开发效率。
