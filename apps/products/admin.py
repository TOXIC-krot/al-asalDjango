from django.contrib import admin
from apps.products import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_available")
