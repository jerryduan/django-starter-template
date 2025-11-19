# 环境配置

本节阐述项目中环境变量的使用方式，并说明如何为开发与生产环境进行配置。

## 环境变量

环境变量用于在不修改代码的情况下配置应用行为，尤其适合管理敏感信息（API Key、数据库凭据）与不同环境（开发/测试/生产）的差异化设置。

项目使用 `django-environ` 从项目根目录的 `.env` 文件读取环境变量。

### `.env.example`

`.env.example` 是 `.env` 的模板，列出项目所需变量的示例与说明。**请勿将实际 `.env` 提交到版本库。**

```ini
# --------------------------------------------------------------------------------
# ⚡ 基础配置：用于开发与测试
# --------------------------------------------------------------------------------
DEBUG=True
DATABASE_URL=postgres://postgres:postgres@localhost:5432/postgres
DJANGO_SECRET_KEY=django-insecure-wlgjuo53y49%-4y5(!%ksylle_ud%b=7%__@9hh+@$d%_^y3s!


# --------------------------------------------------------------------------------
# 📧 邮件配置：可选，如需可复制
# --------------------------------------------------------------------------------
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=user@user.com
EMAIL_HOST_PASSWORD=myverystrongpassword


# --------------------------------------------------------------------------------
# 🔐 安全配置：用于生产或本地验证生产设置
# --------------------------------------------------------------------------------
ALLOWED_HOSTS=mysite.com,mysite2.com
CORS_ALLOWED_ORIGINS=mysite.com,mysite2.com
SENTRY_DSN=https://examplePublicKey@o0.ingest.sentry.io/0
```

设置环境时，将 `.env.example` 复制为 `.env` 并填写实际值：

```bash
cp .env.example .env
```

## 开发环境

本地开发通常需要如下变量：

*   `DEBUG=True`：开启调试模式。
*   `DATABASE_URL`：本地数据库连接（如 Docker 中的 PostgreSQL）。
*   `DJANGO_SECRET_KEY`：开发用密钥，可使用示例值。

使用 Dev Container（推荐）时，`.env` 会自动创建并配置为开发环境。

## 生产环境

生产部署需安全与合理地配置如下变量：

*   `DEBUG=False`：生产必须关闭调试模式。
*   `DJANGO_SECRET_KEY`：生成强且唯一的密钥并安全存储。
*   `ALLOWED_HOSTS`：允许的域名列表，生产禁止 `*`。
*   `DATABASE_URL`：生产数据库连接字符串。
*   `CORS_ALLOWED_ORIGINS`：允许跨域来源列表，生产禁止全开放。
*   `SENTRY_DSN`：用于错误与性能监控的 Sentry DSN。
*   `EMAIL_*`：生产环境邮件服务相关配置。

### 生产 `.env` 示例（概念）

```ini
DEBUG=False
DJANGO_SECRET_KEY=your_very_long_and_secure_production_secret_key
ALLOWED_HOSTS=api.yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@db.yourdomain.com:5432/prod_db
CORS_ALLOWED_ORIGINS=https://www.yourdomain.com,https://app.yourdomain.com
SENTRY_DSN=https://your_sentry_public_key@o0.ingest.sentry.io/0
EMAIL_HOST=smtp.sendgrid.net
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your_sendgrid_api_key
```

## 管理环境变量

建议使用部署平台提供的工具（如 Docker Compose、Kubernetes、Heroku、AWS Elastic Beanstalk）管理并注入生产环境变量，避免在代码中暴露敏感信息。
