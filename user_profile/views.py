from .serializers import CarProfileSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import CarProfile, Profile


class CarProfileViewSet(ModelViewSet):
    queryset = CarProfile.objects.all()
    serializer_class = CarProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@api_view(["POST"])
def get_notification_token(request):

    plate = request.data['plate']

    for t in CarProfile.objects.filter(plate=plate):
        token = t.notification_token

    return Response(token)

# @api_view(["POST"])
# def notification_token(request):
#
#     plate = request.data['plate']
#     notificationTokenArray = []
#     for e in Profile.objects.all():
#         if(e.plate)
#         notificationTokenArray.append(e.notification_token)
#
#     return Response(notificationTokenArray)


@api_view(["GET"])
def notification_token(request):

    notificationTokenArray = []
    for e in Profile.objects.all():
        notificationTokenArray.append(e.notification_token)

    return Response(notificationTokenArray)
