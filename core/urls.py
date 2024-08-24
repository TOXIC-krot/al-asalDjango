from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="BRB Titans API",
        default_version="v1",
        description="brb-titans backend api",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# external packages urls
urlpatterns = [
    path("rosetta/", include("rosetta.urls")),
]

# custom urls
urlpatterns += [
    # path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/cart/", include("apps.cart.urls")),
    path("api/v1/products/", include("apps.products.urls")),
    path("api/v1/bot/", include("apps.bot.urls")),
]

# swagger urls
urlpatterns += [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# admin urls
urlpatterns += [
    path("", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
