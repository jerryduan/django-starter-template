# Celery 任务

本节介绍在项目中使用 Celery 的方法，包括创建、配置与管理任务，重点说明重试机制与周期任务。

## 概览

Celery 是基于分布式消息的异步任务队列。本项目使用 Celery 以将耗时操作移出请求主流程，提升响应与可扩展性。

## 配置

Celery 在 `conf/celery.py` 中配置，并与 Django 设置集成。

关键设置位于 `conf/settings.py`：

*   `CELERY_BROKER_URL`：消息代理 URL（如 Redis）
*   `CELERY_RESULT_BACKEND`：任务结果存储（如 Django 数据库）
*   `CELERY_BEAT_SCHEDULER`：周期任务调度器

## 创建新任务

使用 `@shared_task` 创建新任务：

```python
from celery import shared_task

@shared_task
def my_new_task(arg1, arg2):
    # Your task logic here
    print(f"Executing my_new_task with {arg1} and {arg2}")
```

将任务定义放在各应用的 `tasks.py`（如 `apps/core/tasks.py`）。Celery 会自动发现。

## 任务重试

模板提供 `apps/core/tasks.py` 中的任务基类 `BaseTaskWithRetry`，简化重试逻辑实现。

### `BaseTaskWithRetry` 属性

*   `autoretry_for`：触发自动重试的异常类型集合。
*   `retry_kwargs`：传递给 `retry()` 的参数，如 `max_retries`。
*   `retry_backoff`：首次重试前的延迟（秒），后续指数增加。
*   `retry_jitter`：是否添加随机抖动，避免“惊群效应”。

### 使用示例

将任务的 `base` 设置为 `BaseTaskWithRetry`：

```python
from celery import shared_task
from apps.core.tasks import BaseTaskWithRetry

@shared_task(bind=True, base=BaseTaskWithRetry)
def my_retriable_task(self):
    try:
        # Your task logic that might fail
        result = 1 / 0 # Example of an error
        return result
    except Exception as e:
        # Log the error or perform any necessary cleanup before retrying
        print(f"Task failed: {e}. Retrying...")
        raise self.retry(exc=e)
```

## 调用任务

调用任务的常见方式：

*   **异步调用（推荐）：**

    ```python
    my_new_task.delay(arg1_value, arg2_value)
    ```

*   **带更多控制（倒计时或 ETA）：**

    ```python
    from datetime import datetime, timedelta

    # Execute in 10 seconds
    my_new_task.apply_async((arg1_value, arg2_value), countdown=10)

    # Execute at a specific time
    eta_time = datetime.now() + timedelta(minutes=5)
    my_new_task.apply_async((arg1_value, arg2_value), eta=eta_time)
    ```

## 周期任务

Celery Beat 用于周期性执行任务。本项目可通过 Django Admin 管理周期任务。

### 配置周期任务步骤

1.  **启动 Celery Worker**：

    ```bash
    poetry run worker
    ```

2.  **启动 Celery Beat**：

    ```bash
    poetry run beat
    ```

3.  **在 Django Admin 配置**：访问 `/admin-panel/`，在 `DJANGO CELERY BEAT` 下新增与管理 `Periodic tasks`，指定：
*   任务名称（如 `apps.core.tasks.my_periodic_task`）
*   调度频率（每 5 分钟、每日等）
*   任务参数或关键字参数

### Example Periodic Task

```python
from celery import shared_task

@shared_task
def my_periodic_task():
    print("This task runs periodically!")
```
