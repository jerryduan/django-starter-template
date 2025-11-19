# 核心应用（Core）

## 概览

核心应用（`apps/core/`）提供项目基础能力：通用工具、中间件、任务基类与关键 API 端点。

## 关键功能

`apps/core/` 包含以下功能：

*   **Middleware**：如 `RequestIDMiddleware`，为日志与响应注入 `request_id`、客户端 IP、响应时间等信息。
*   **Tasks**：Celery 任务基类 `BaseTaskWithRetry`，提供自动重试等通用能力。
*   **Schema**：通用 OpenAPI 组件与示例，提升文档复用与一致性。
*   **管理命令**：如 `seed`，用于开发与测试阶段批量生成示例数据。

## API 端点

核心应用暴露以下端点（统一前缀 `/core/`）：

### Ping

用于检查服务器是否正常响应的简易端点。

**请求：**

*   **Method:** `GET`
*   **URL:** `/core/ping/`

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "ping": "pong"
    }
    ```
    *   返回 `{"ping":"pong"}`，表示正常响应。

### Fire Task

触发示例 Celery 任务，用于测试任务执行与队列配置。

**请求：**

*   **Method:** `GET`
*   **URL:** `/core/fire-task/`

**响应：**

*   **成功（200 OK）：**
    ```json
    {
        "task": "Task fired"
    }
    ```
    *   返回任务已触发的确认信息。