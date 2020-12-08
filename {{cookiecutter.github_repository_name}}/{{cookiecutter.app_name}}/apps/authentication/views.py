from rest_framework_simplejwt.views import TokenObtainPairView

from {{cookiecutter.app_name}}.apps.authentication.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
