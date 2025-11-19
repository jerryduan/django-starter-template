# 日志系统

本节介绍项目的日志系统，包括配置、特性与如何理解日志内容。

## 概览

日志系统在 `conf/settings.py` 统一配置，输出结构化且全面的日志，便于监控、调试与分析，尤其适合生产环境。

## 关键特性

*   **JSON 格式**：日志使用 JSON 格式，易于解析与接入日志平台。
*   **多处理器与文件**：按类型分别输出到 `console`、`app.log`、`security.log`、`error.log`、`info.log`。
*   **文件轮转**：单文件最大 10MB，保留 5 个备份，避免无限增长。
*   **请求追踪**：`RequestIDMiddleware` 为每次请求注入 `request_id`、客户端 IP、请求路径、用户 ID、响应时间与状态码。
*   **Sentry 集成**：生产环境启用 Sentry 进行错误与性能监控。

## 日志位置

日志位于项目根目录的 `logs/`：

*   `logs/app.log`：通用应用日志
*   `logs/security.log`：认证与安全事件
*   `logs/error.log`：错误日志
*   `logs/info.log`：信息级日志

## 日志示例

日志为 JSON 格式，包含丰富上下文信息：

```json
{
    "asctime": "2025-05-04 14:17:22,365",
    "levelname": "INFO",
    "module": "views",
    "process": 5929,
    "thread": 281473186128320,
    "message": "Ping request received",
    "client": "127.0.0.1",
    "request_id": "0d7344bd-0e6f-426d-aeed-46b9d1ca36bc",
    "path": "/core/ping/",
    "user_id": 1,
    "status_code": 401,
    "response_time": 0.0019102096557617188
}
```

各字段含义：

*   `asctime`：时间戳
*   `levelname`：日志级别
*   `module`：模块名
*   `process`：进程 ID
*   `thread`：线程 ID
*   `message`：日志消息
*   `client`：客户端 IP
*   `request_id`：请求唯一 ID
*   `path`：请求路径
*   `user_id`：用户 ID（未认证为 anonymous）
*   `status_code`：响应状态码
*   `response_time`：处理耗时（秒）
