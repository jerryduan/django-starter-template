# 测试

项目以 `pytest` 作为主要测试框架，结合 `pytest-django` 进行 Django 测试，并通过 `pytest-cov` 实现覆盖率统计，提供稳健高效的测试环境。

## 测试配置

### `pytest.ini` 配置

项目根目录的 `pytest.ini` 用于配置 `pytest` 行为：

```ini
[pytest]
DJANGO_SETTINGS_MODULE = conf.test_settings
python_files = tests.py test_*.py *_tests.py

addopts = --reuse-db --nomigrations --cov=. --cov-report=html --cov-report=term-missing --no-cov-on-fail
```

*   `DJANGO_SETTINGS_MODULE = conf.test_settings`：使用专用测试设置文件。
*   `python_files = tests.py test_*.py *_tests.py`：测试文件发现规则。
*   `addopts`：常用选项：
    *   `--reuse-db`：复用测试数据库，加速后续运行。
    *   `--nomigrations`：测试时跳过迁移。
    *   `--cov=.`：启用覆盖率统计。
    *   `--cov-report=html`：生成覆盖率 HTML 报告。
    *   `--cov-report=term-missing`：终端显示缺失覆盖信息。
    *   `--no-cov-on-fail`：失败时不输出覆盖率。

### 测试文件组织

测试按应用分布在各自的 `tests/` 目录，如 `apps/users/tests/`。

*   `apps/core/tests/`：核心功能测试
*   `apps/users/tests/`：用户与认证测试

This structure keeps tests co-located with the code they test, making it easier to find and maintain them.

## 运行测试

运行测试可使用 `poetry run pytest`，`pytest.ini` 将自动生效。

### 基本运行

运行全部测试：

```bash
poetry run pytest
```

### 覆盖率统计

运行测试并生成覆盖率报告：

```bash
poetry run pytest --cov
```

终端会输出覆盖率摘要；如需详细的 HTML 报告：

```bash
poetry run pytest --cov --cov-report=html
```

HTML 报告位于项目根目录 `htmlcov/`。

### 运行指定测试

支持运行特定测试文件或函数：

*   **运行某个文件：**

    ```bash
    poetry run pytest apps/users/tests/test_user_model.py
    ```

*   **运行某个测试函数：**

    ```bash
    poetry run pytest apps/users/tests/test_user_model.py::test_create_user
    ```

## 最佳实践

*   **覆盖率**：关注关键逻辑与接口的覆盖率。
*   **Fixtures**：使用 fixtures 复用准备数据与环境。
*   **命名清晰**：如 `test_feature_name.py`、`test_function_behavior`。
*   **隔离性**：测试互不依赖，使用事务或清理机制。
