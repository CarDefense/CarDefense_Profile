from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Profile
import requests
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from rest_framework import permissions, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


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


# added
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
