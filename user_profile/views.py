from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Profile
import requests


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@api_view(["POST"])
def set_token(request):

    id_token = request.data['id_token']
    notification_token = request.data['notification_token']
    i = 0
    index = ''

    for t in Profile.objects.filter(id_token=id_token):
        if(id_token == t.id_token):
            i += 1
            index = t.id

    if(i):
        task = {"notification_token": notification_token}
        url = 'http://cardefense2.eastus.cloudapp.azure.com:8005/profiles/'+str(index)+'/'
        resp = requests.patch(url, json=task)
        return Response(resp)

    else:
        task = {"id_token": id_token, "notification_token": notification_token}
        resp = requests.post('http://cardefense2.eastus.cloudapp.azure.com:8005/profiles/', json=task)
        return Response(resp)


@api_view(["GET"])
def notification_token(request):

    notificationTokenArray = []
    for e in Profile.objects.all():
        notificationTokenArray.append(e.notification_token)

    return Response(notificationTokenArray)


@api_view(["POST"])
def get_notification_token(request):

    id_token = request.data['token']
    for t in Profile.objects.filter(id_token=id_token):
        token = t.notification_token
    return Response(token)
