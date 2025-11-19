# 项目结构

## 概览

掌握项目的目录结构有助于高效导航、开发与维护。本文档对主要目录与文件进行说明，帮助快速理解整体组织方式。

```
├── .clinerules/                # Gemini CLI rules
├── .coveragerc                 # Coverage.py configuration
├── .devcontainer/              # Dev container configuration
├── .env.example                # Example environment variables file
├── .flake8                     # Flake8 linter configuration
├── .github/                    # GitHub CI/CD workflows and issue templates
├── .gitignore                  # Git ignore file
├── .pytest_cache/              # Pytest cache
├── .venv/                      # Virtual environment
├── .vscode/                    # VS Code settings and recommended extensions
├── apps/                       # Django applications (core logic)
│   ├── core/                   # Core functionalities and shared components
│   │   ├── __init__.py         # Initializes the core app
│   │   ├── admin.py            # Django admin configuration for core app
│   │   ├── apps.py             # App configuration for core app
│   │   ├── management/         # Custom Django management commands
│   │   ├── middleware.py       # Custom middleware for core app
│   │   ├── migrations/         # Database migrations for core app
│   │   ├── schema.py           # OpenAPI schema definitions for core app
│   │   ├── tasks.py            # Celery task definitions for core app
│   │   ├── tests/              # Unit and integration tests for core app
│   │   └── urls.py             # URL routing for core app
│   └── users/                  # User management and authentication app
│       ├── __init__.py         # Initializes the users app
│       ├── admin.py            # Django admin configuration for users app
│       ├── apps.py             # App configuration for users app
│       ├── forms.py            # Custom forms for users app
│       ├── managers.py         # Custom managers for user models
│       ├── migrations/         # Database migrations for users app
│       ├── models.py           # User model definition
│       ├── schema.py           # OpenAPI schema definitions for users app
│       ├── serializers.py      # Serializers for users app
│       ├── tests/              # Unit and integration tests for users app
│       ├── throttles.py        # Rate limiting configurations for user-related views
│       ├── urls.py             # URL routing for users app
│       ├── utils.py            # Utility functions for users app
│       └── views.py            # API views for user authentication and profile management
├── conf/                       # Project-wide configuration
│   ├── __init__.py             # Initializes the conf module
│   ├── asgi.py                 # ASGI application entry point
│   ├── celery.py               # Celery application configuration
│   ├── settings.py             # Main Django settings file
│   ├── test_settings.py        # Settings specifically for running tests
│   ├── test_utils.py           # Test utilities
│   ├── urls.py                 # Main URL routing for the project
│   └── wsgi.py                 # WSGI application entry point
├── docs/                       # Documentation files
├── logs/                       # Application log files
├── manage.py                   # Django's command-line utility
├── mkdocs.yml                  # MkDocs configuration
├── notebook.ipynb              # Jupyter Notebook for interactive development
├── poetry.lock                 # Poetry lock file
├── pyproject.toml              # Project dependencies and metadata (Poetry)
├── pytest.ini                  # Pytest configuration
├── README.md                   # Project README file
├── renovate.json               # Renovate Bot configuration for dependency updates
├── scripts/                    # Utility scripts for various development tasks
├── static/                     # Static files (CSS, JavaScript, images)
└── templates/                  # Project-wide HTML templates
```

## 关键目录

This section describes the primary directories within the project and their respective purposes:

*   **`.devcontainer/`**：VS Code Dev Container 配置，提供一致、可复现的开发环境。

*   **`.github/`**：GitHub 相关配置，含 Actions 工作流、模板与仓库设置。

*   **`.vscode/`**：VS Code 工作区设置与推荐扩展，统一格式化、Lint 与调试配置。

*   **`apps/`**：Django 应用模块所在目录，面向特定功能的可复用单元。
    *   **`core/`**：基础能力与通用组件（管理命令、Celery 任务基类、通用 OpenAPI Schema 等）。
    *   **`users/`**：用户认证与授权（模型、序列化器、视图与相关工具）。

*   **`conf/`**：项目级配置（`settings.py`、`urls.py`、ASGI/WSGI、Celery）。

*   **`logs/`**：应用日志目录，区分不同日志类型便于监控与排障。

*   **`scripts/`**：自动化与维护脚本（运行服务器、迁移等）。

*   **`static/`**：静态资源（CSS/JS/图片）。

*   **`templates/`**：项目级 HTML 模板（错误页、基础布局等）。

## 关键文件

This section outlines the most important files at the project root and their functions:

*   **`.env.example`**：环境变量示例模板，复制为 `.env` 并填写实际值。

*   **`manage.py`**：Django 命令行工具，用于运行服务、迁移、创建超管与管理命令等。

*   **`pyproject.toml`**：Poetry 的项目元数据与依赖配置文件。

*   **`pytest.ini`**：`pytest` 测试配置，包含覆盖率与发现规则。

*   **`README.md`**：项目概览与快速开始指南，关键特性与文档链接。

遵循以上结构可提升模块化、可维护性与可扩展性，方便团队理解与协作。
