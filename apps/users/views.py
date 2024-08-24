from rest_framework import generics
from django.contrib.auth import get_user_model

from apps.users.serializers import SignUpSerializer, UserProfileSerializer


User = get_user_model()


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
