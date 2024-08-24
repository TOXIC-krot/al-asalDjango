from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

from apps.users.views import SignUpView, UserProfileView

from django.urls import path


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
