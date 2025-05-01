from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


# TODO 🚫 Delete the index view, route and template.
def index(request):
    base_url = (
        "https://github.com/wilfredinni/django-starter-template?tab=readme-ov-file"
    )
    context = {}
    context["version"] = "0.2.8"
    context["buttons"] = [
        {"title": "🚀 Features", "url": f"{base_url}#key-features"},
        {"title": "📋 Requirements", "url": f"{base_url}#requirements"},
        {"title": "🛠️ API Schema", "url": "/api/schema/swagger-ui/"},
    ]
    return render(request, "index.html", context)


# API v1 endpoints
api_v1_patterns = [
    path("auth/", include("apps.users.urls")),
    path("core/", include("apps.core.urls")),
]

urlpatterns = [
    # TODO⚡ Change the admin url to one of your choice.
    # Please avoid using the default 'admin/' or 'admin-panel/'
    path("admin-panel/", admin.site.urls, name="admin"),
    # API versioning
    path("api/v1/", include((api_v1_patterns, "v1"), namespace="v1")),
    path("", index),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
