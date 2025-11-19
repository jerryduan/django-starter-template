# GitHub Copilot

本页提供在本项目中使用 GitHub Copilot 的详细说明与指南。

## 技术要求与沟通规范

在使用 Copilot 进行 Django 后端开发时，本项目遵循以下技术要求与沟通规范：

**框架与核心依赖：**
- Django 5.2+ 与 DRF
- PostgreSQL 数据库
- Redis 缓存
- 认证使用 django-rest-knox
- API 文档使用 drf-spectacular
- 测试框架：Pytest 或 Django/DRF TestCase

**项目结构：**
- 测试文件置于各应用的 `tests` 目录
- 遵循 Django 推荐的项目布局
- 实现 RESTful API 模式

**开发指南：**
1. 遵循 Django 最佳实践与安全标准
2. 构建 API 时使用 DRF 的 viewsets 与 serializers
3. 使用 knox 实现认证与权限校验
4. 对昂贵操作使用 Redis 缓存
5. 通过 drf-spectacular 使用 OpenAPI/Swagger 记录接口

**测试要求：**
1. 为所有功能编写全面的单元测试
2. 遵循 Pytest 约定与模式
3. 达到项目规定的最低覆盖率
4. 同时覆盖正向与异常场景

**文档：**
1. 参考官方 Django 与 DRF 文档
2. 为重要类与方法编写 docstring
3. 使用 drf-spectacular 装饰器记录 API 端点

**回答格式：**
1. 提供直接、面向实现的答案
2. 指出实现所需但缺失的信息
3. 仅在明确请求时提供代码示例
4. 遵循 PEP 8 代码风格

- 在适用时利用 context7 MCP 获取当前文档

所有回答需聚焦在上述规范下的技术实现，避免理论化讨论或无关技术建议。



### Feature Prompt（`feature.prompt.md`）

**用途：** 规划与实现新功能时使用，引导 Copilot 从概览、影响、实施计划、代码到集成策略进行思考。

```markdown
As a professional developer, analyze and implement a new feature in the codebase following these guidelines:

1. Feature Overview
   - Describe the feature's core functionality and purpose
   - List specific requirements and acceptance criteria
   - Define expected inputs and outputs
   - Specify performance targets and constraints

2. Impact Analysis
   - Identify affected components and dependencies
   - Evaluate performance implications
   - Assess security considerations
   - Document potential risks and mitigations

3. Implementation Plan
   - Break down the feature into atomic tasks
   - Specify interfaces and data structures
   - Define error handling and edge cases
   - List required test scenarios

4. Code Implementation
   - Provide code examples for each component
   - Include inline documentation
   - Follow project coding standards
   - Implement necessary unit tests

5. Integration Strategy
   - Outline deployment steps
   - Specify configuration changes
   - Document API modifications
   - Define rollback procedures

Include benchmark results, security review findings, and maintainability metrics for each implemented component. Prioritize clean architecture and SOLID principles.
```

### Refactor Prompt（`refactor.prompt.md`）

**用途：** 重构既有代码时使用，使 Copilot 聚焦性能、安全、可维护性与可读性并提供结构化改进建议。

```markdown
As a senior software engineer, analyze the provided code and suggest specific refactoring improvements focusing on these key aspects:

1. Performance:
- Identify algorithmic inefficiencies
- Optimize resource usage and memory management
- Suggest caching strategies where applicable
- Highlight potential bottlenecks

2. Security:
- Review for common vulnerabilities (OWASP Top 10)
- Ensure proper input validation
- Verify authentication and authorization
- Check for secure data handling

3. Maintainability:
- Apply SOLID principles
- Improve code organization and structure
- Reduce technical debt
- Enhance modularity and reusability

4. Readability:
- Follow language-specific style guides
- Apply consistent naming conventions
- Add meaningful comments and documentation
- Break down complex logic into smaller functions

For each suggested improvement:
- Explain the rationale
- Provide a code example
- Highlight potential trade-offs
- Consider the impact on existing functionality

Please provide the code you want to refactor, and specify any constraints or requirements specific to your project's context.
```

### Security Prompt（`security.prompt.md`）

**用途：** 用于进行 API 安全审查，引导 Copilot 检查认证、授权、输入校验、限流与安全监控。

```markdown
Conduct a comprehensive security review of the REST API implementation according to industry best practices. Review and implement the following security controls:

Authentication & Authorization:
- Verify JWT/OAuth2 authentication is properly implemented for all endpoints
- Confirm role-based access control (RBAC) is enforced
- Check token validation, expiration, and refresh mechanisms
- Ensure sensitive endpoints require appropriate scopes/permissions

Input Validation & Sanitization:
- Validate request parameters, headers, and body content
- Implement strong input validation using a schema validator (e.g. JSON Schema)
- Apply appropriate encoding for special characters
- Prevent SQL injection, XSS, and CSRF attacks

Rate Limiting & DDoS Protection:
- Set appropriate rate limits per endpoint/user
- Implement exponential backoff for failed attempts
- Configure API gateway throttling rules
- Document rate limit headers and responses

Security Monitoring:
- Enable detailed logging for authentication attempts
- Track and alert on suspicious activity patterns
- Log all administrative actions and data modifications
- Implement audit trails for sensitive operations
- Set up automated security scanning and penetration testing

Follow OWASP API Security Top 10 guidelines and document any findings in a security assessment report.

References:
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
- NIST Security Guidelines for Web Services
```

### Test Model Prompt（`test-model.prompt.md`）

**用途：** 为 Django 模型编写测试时使用，确保字段校验、关系、数据操作、边界与性能的全面覆盖。

```markdown
Write comprehensive model tests for Django applications adhering to the following specifications:

## Test Structure
- Organize tests in `tests/test_<model_name>.py` within each Django app
- Implement tests using pytest or Django TestCase
- Follow PEP 8 and Django coding standards

## Required Test Coverage

### 1. Field Validation
- Test all model field constraints:
  - Required fields (null/blank)
  - Field type validations
  - Length/range restrictions
  - Custom validators
  - Unique constraints
  - Index effectiveness

### 2. Relationships
- Validate ForeignKey constraints
- Test ManyToMany relationship behaviors
- Verify cascading operations
- Check related field access patterns

### 3. Data Operations
- Test CRUD operations
- Verify bulk operations performance
- Validate custom manager methods
- Test model-specific business logic
- Check complex queries and filters

### 4. Edge Cases
- Test boundary conditions
- Include negative test scenarios
- Validate error handling
- Check race conditions

### 5. Performance
- Benchmark query execution times
- Test with representative data volumes
- Verify index usage
- Monitor memory consumption

## Documentation
- Add descriptive docstrings
- Document test fixtures
- Explain complex test scenarios
- Reference expected behaviors

## References
- Django Testing Documentation: https://docs.djangoproject.com/en/stable/topics/testing/
- pytest-django: https://pytest-django.readthedocs.io/

Use appropriate fixtures and mocking strategies to ensure tests are isolated and repeatable.
```

### Test View Prompt（`test-view.prompt.md`）

**用途：** 为 DRF 视图编写测试时使用，确保认证、安全、HTTP 方法、响应校验与边界场景的全面覆盖。

```markdown
Generate comprehensive test suite for Django REST framework API views following these requirements:

1. Test Location and Framework:
   - Place tests in the `tests` directory within each Django app
   - Use Pytest or Django/DRF TestCase as the testing framework
   - Follow the `test_<view_name>.py` naming convention

2. Authentication & Security Tests:
   - Verify authentication requirements for each endpoint
   - Test authorization rules and permissions
   - Validate rate limiting functionality
   - Test request throttling behavior

3. HTTP Method Coverage:
   - Test all CRUD operations: GET, POST, PUT, PATCH, DELETE
   - Verify correct HTTP status codes (200, 201, 204, 400, 401, 403, 404, etc.)
   - Include both successful and error scenarios
   - Test request payload validation

4. Response Validation:
   - Verify response structure and data types
   - Check serializer field validation
   - Test pagination if implemented
   - Validate filtering and sorting functionality

5. Documentation Requirements:
   - Include docstrings describing test purpose
   - Document test data and fixtures
   - Add comments for complex test scenarios

6. Edge Cases:
   - Test boundary conditions
   - Include negative testing scenarios
   - Verify error message formats

Reference Django REST framework testing documentation for best practices:
https://www.django-rest-framework.org/api-guide/testing/
```

## 可复用 Prompts

针对不同任务的可复用 Prompts 位于 [.github/prompts/](../../.github/prompts/)：
*   `feature.prompt.md`
*   `refactor.prompt.md`
*   `security.prompt.md`
*   `test-model.prompt.md`
*   `test-view.prompt.md