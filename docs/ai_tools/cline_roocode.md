# Roo Code 与 Cline

本页说明 Cline 在本项目中针对 Django 后端开发的规则与最佳实践。完整最新规则请参考项目根目录的 `.clinerules/django-backend-rules.md`。

## 简要概览
本文档概述 Django 后端开发的规则与最佳实践，涵盖框架使用、项目结构、测试与文档等。

## 框架与核心依赖
- 使用 Django 5.2+ 与 DRF 构建 API
- 数据库默认使用 PostgreSQL
- 对昂贵操作使用 Redis 缓存
- 使用 django-rest-knox 进行认证
- 使用 drf-spectacular 记录 API 文档

## 项目结构
- 严格遵循 Django 推荐的项目布局
- 保持应用模块化与单一职责
- 在每个应用的 `tests` 目录中放置测试文件
- 一致地实现 RESTful API 模式

## 开发实践
- 严格遵循 Django 安全标准
- 端点使用 DRF 的 viewsets 与 serializers
- 使用 knox 实现正确的认证
- 使用 Redis 缓存昂贵操作
- 通过 drf-spectacular 以 OpenAPI/Swagger 记录接口

## 测试要求
- 为所有功能编写全面的单元测试
- 达到规定的最小覆盖率
- 覆盖正向与异常场景
- 测试文件与被测代码同目录维护

## 文档标准
- 为重要类/方法编写 docstring
- 详细记录 API 端点
- 文档随代码保持更新
- 参考官方 Django/DRF 文档

## 其他指引
- 优先使用 Django 原生方案
- 变更时关注向后兼容性
- 严格校验所有用户输入
- 实现完备的错误处理与日志记录
