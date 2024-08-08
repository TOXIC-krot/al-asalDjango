from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render


def tailwind_sample(request):
    return render(request, "sample.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include("apps.cart.urls")),
    path("user/", include("apps.user.urls")),
    path("tailwind/", tailwind_sample, name="tailwind_sample"),
    path("", include("apps.index.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
