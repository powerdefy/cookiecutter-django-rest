from rest_framework import viewsets

from {{cookiecutter.app_name}}.apps.profiles.filters import ProfileFilter
from {{cookiecutter.app_name}}.apps.profiles.models import Profile
from {{cookiecutter.app_name}}.apps.profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    filter_class = ProfileFilter
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('first_name', 'last_name')
