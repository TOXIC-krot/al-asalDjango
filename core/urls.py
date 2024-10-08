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
        title="Al Asal API",
        default_version="v1",
        description="al-asal backend api",
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

# order
urlpatterns = [
    path("orders/", include("apps.orders.urls")),
]

# custom urls
urlpatterns += [
    path("api/users/", include("apps.users.urls")),
    # path("api/cart/", include("apps.cart.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/bot/", include("apps.bot.urls")),
    path("api/favorites/", include("apps.favorites.urls")),
    # new urls
    path("api/ecommerce/", include("apps.ecommerce.urls")),
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
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
