# API 自动文档

## 概览

本节介绍项目的自动化 API 文档方案，基于 `drf-spectacular` 生成 OpenAPI 3（Swagger）文档，使文档与代码保持同步，降低维护成本并避免不一致。

## 什么是 `drf-spectacular`？

`drf-spectacular` 与 DRF 深度集成，可从视图、序列化器等组件生成完整的 OpenAPI Schema，并用于渲染交互式文档（如 Swagger UI）或生成客户端 SDK。

## 在项目中的使用（最佳实践）

模板遵循最佳实践以产出丰富且准确的 API 文档。

### 1. 统一的 Schema 定义

项目将可复用的 Schema 组件（如错误响应与通用示例）集中放在各应用的 `schema.py`，而非散落在视图中，从而提升复用性并保持视图简洁。

```python
# Example from apps/core/schema.py
from drf_spectacular.utils import OpenApiExample, inline_serializer
from rest_framework import serializers

ErrorResponseSerializer = inline_serializer(
    name="ErrorResponse",
    fields={
        "detail": serializers.CharField(read_only=True),
        "code": serializers.CharField(read_only=True, required=False),
    },
)

UNAUTHORIZED_EXAMPLES = [
    OpenApiExample(
        "Unauthorized",
        value={"detail": "Authentication credentials were not provided."},
        status_codes=["401"],
    ),
    # ... other examples
]
```

### 2. 视图使用 `extend_schema`

在 API 视图上使用 `extend_schema` 补充 `drf-spectacular` 难以自动推断的元数据，包括：

*   **响应**：成功与错误响应，通常引用集中定义的 Schema
*   **请求体**：明确请求负载结构
*   **参数**：记录查询参数、路径参数与头部
*   **描述**：添加端点说明

**Example (from `apps/users/views.py` for LoginView):**

```python
from drf_spectacular.utils import extend_schema
# ... other imports

@extend_schema(responses=LOGIN_RESPONSE_SCHEMA)
class LoginView(KnoxLoginView):
    # ... view implementation
```

此处的 `LOGIN_RESPONSE_SCHEMA` 来自 `apps/users/schema.py`，保证一致性与复用。

### 3. `conf/settings.py` 中的 `SPECTACULAR_SETTINGS`

在 `conf/settings.py` 的 `SPECTACULAR_SETTINGS` 中配置全局参数，如标题、描述与版本号。

```python
# Example from conf/settings.py
SPECTACULAR_SETTINGS = {
    "TITLE": "Django Starter Template",
    "DESCRIPTION": "A comprehensive starting point for your new API with Django and DRF",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
```

### 4. 交互式 Swagger UI

OpenAPI Schema 将通过 Swagger UI 提供交互式文档界面，便于探索与测试 API：

`/api/schema/swagger-ui/`

该端点在 `conf/urls.py` 中配置：

```python
# Example from conf/urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # ... other urls
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
```

遵循以上实践，文档将保持健壮、易维护且自动生成，真实反映 API 状态。
