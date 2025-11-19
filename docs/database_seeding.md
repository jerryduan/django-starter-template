# 数据库灌数据（Seeding）

数据库灌数据指向数据库填充初始或示例数据。在开发与测试阶段尤为有用，可快速获得真实感数据而无需手动录入。

## 为什么需要灌数据？

*   **开发**：快速搭建带示例数据的环境，立即进入功能开发。
*   **测试**：保证测试基于一致且具代表性的数据集，提高可靠性与可复现性。
*   **演示**：方便准备演示或展示用数据。

## `seed` 管理命令

项目提供自定义管理命令 `seed`（路径：`apps/core/management/commands/seed.py`），用于快速填充示例用户数据。

### 用法

通过 `python manage.py seed` 或 `poetry run seed` 运行。

```bash
python manage.py seed [options]
```

### 可用参数

The `seed` command supports the following arguments:

*   `--users <count>`：创建的假用户数量，默认 10。
    *   **示例：** `python manage.py seed --users 50`

*   `--superuser`：创建默认超管（`admin@admin.com` / `admin`）。
    *   **示例：** `python manage.py seed --superuser`

*   `--clean`：在灌数据前删除现有（非超管）用户数据，适合从空数据集开始。
    *   **示例：** `python manage.py seed --clean`

### 组合示例

You can combine these options to achieve specific seeding scenarios:

*   **基本灌数据（创建 10 用户）：**

    ```bash
    python manage.py seed
    ```

*   **创建指定数量用户并添加超管：**

    ```bash
    python manage.py seed --users 20 --superuser
    ```

*   **清理数据，创建 50 用户并添加超管：**

    ```bash
    python manage.py seed --users 50 --superuser --clean
    ```

## 实现细节

`seed` 命令使用 `Faker` 生成逼真的假数据，并通过 `transaction.atomic` 保证灌数据过程的原子性：任一步骤失败将回滚，避免产生不一致数据。
