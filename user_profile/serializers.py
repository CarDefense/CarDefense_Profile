from rest_framework.serializers import ModelSerializer
from .models import CarProfile, Profile


class CarProfileSerializer(ModelSerializer):
    class Meta:
        model = CarProfile
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
