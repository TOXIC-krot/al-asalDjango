from django.contrib import admin
from apps.users.models import User

# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    pass
