from django.urls import path
from .views import save_user_info, check_user, update_last_active, token_login
from index.views import product_list  # CHECKOUT

urlpatterns = [
    path('api/save_user_info/', save_user_info, name='save_user_info'),
    path('api/check_user/', check_user, name='check_user'),
    path('api/update_last_active/', update_last_active, name='update_last_active'),
    path('token_login/', token_login, name='token_login'),
    path('product_list/', product_list, name='product_list')  # CHECKOUT
]
