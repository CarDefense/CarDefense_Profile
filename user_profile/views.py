from .serializers import CarProfileSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import CarProfile, Profile
import requests


class CarProfileViewSet(ModelViewSet):
    queryset = CarProfile.objects.all()
    serializer_class = CarProfileSerializer

    def get_queryset(self):
        token = self.request.query_params.get("token")
        return CarProfile.objects.filter(notification_token=token)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@api_view(["POST"])
def set_notification_token(request):

    token = request.data['token']
    i=0
    for t in Profile.objects.filter(notification_token=token):
        if(token==t.notification_token):
            i+=1

    if(i==0):
        task = {"notification_token": token}
        resp = requests.post('http://68.183.28.199:8005/profiles/', json=task)
        return Response(resp)
    return Response("Já cadastrado")


@api_view(["POST"])
def get_notification_token(request):

    plate = request.data['plate']

    for t in CarProfile.objects.filter(plate=plate):
        token = t.notification_token

    return Response(token)


# @api_view(["POST"])
# def get_cars(request):
#
#     notification_token = request.data['notification_token']
#
#     cars = []
#     for t in CarProfile.objects.filter(notification_token=notification_token):
#         cars.append(t.plate)
#
#     return Response(cars)

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
