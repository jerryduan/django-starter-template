# 开发流程

## 概览

本文档概述在 Django Starter Template 中进行开发的关键命令与最佳实践，建议在 Dev Container 环境下完成初始设置后再开始。

## 核心开发命令

项目通过 `pyproject.toml` 提供便捷的 `poetry run` 脚本，以简化常见的开发操作。建议在 VS Code Dev Container 或已激活的 Poetry Shell 中运行这些命令。

| 命令 | 说明 |
| :--- | :--- |
| `poetry run server` | 启动 Django 开发服务器 |
| `poetry run makemigrations` | 根据模型变更生成迁移 |
| `poetry run migrate` | 应用待处理的数据库迁移 |
| `poetry run test` | 使用 `pytest` 运行测试套件 |
| `poetry run test-cov`| 运行测试并生成覆盖率报告 |

### 测试

项目使用 `pytest` 进行测试。以下为常用命令：

*   **运行全部测试：**
    ```bash
    poetry run pytest
    ```
    执行完整测试套件。

*   **带覆盖率运行测试：**
    ```bash
    poetry run pytest --cov
    ```
    运行全部测试并收集覆盖率信息。

*   **生成 HTML 覆盖率报告：**
    ```bash
    poetry run pytest --cov --cov-report=html
    ```
    生成详细的覆盖率 HTML 报告，位于 `htmlcov/` 目录。

## 数据库灌数据（Seeding）

模板提供了用于填充示例数据的管理命令，适用于开发与测试。在 `apps/core/management/commands/seed.py`。

**用法：**

```bash
# 基本灌数据（默认创建 10 个用户）
poetry run seed

# 创建指定数量的用户
poetry run seed --users 20

# 创建超管（admin@admin.com:admin）
poetry run seed --superuser

# 在灌数据前清理现有数据
poetry run seed --clean

# 组合使用示例
poetry run seed --users 50 --superuser --clean
```

**选项：**

*   `--users <number>`：创建的普通用户数量，默认 10。
*   `--superuser`：创建默认超管（`admin@admin.com` / `admin`）。
*   `--clean`：在灌数据前清理已有数据（谨慎使用）。

## 异步任务（Celery）

项目集成 Celery 以处理后台与异步任务。使用以下命令运行：

*   **启动 Celery worker：**
    ```bash
    poetry run worker
    ```
    启动 Celery worker 以消费队列中的任务。

*   **启动 Celery beat 调度：**
    ```bash
    poetry run beat
    ```
    启动 Celery beat，负责定时调度周期任务。

## 环境变量

项目使用 `.env` 管理环境变量，以避免在代码中硬编码敏感信息，并通过 `django-environ` 加载。

*   **开发环境 `.env`：** 使用 `poetry run create_dev_env` 生成开发用 `.env`。
*   **生产环境 `.env`：** 参考项目根目录的 `.env.example`，根据说明配置实际变量。
