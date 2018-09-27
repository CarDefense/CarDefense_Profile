from .serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Profile


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
