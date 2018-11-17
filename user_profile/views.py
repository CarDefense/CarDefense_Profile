from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Profile, Document
from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, DocumentSerializer
from rest_framework.decorators import permission_classes


class ProfileViewSet(ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DocumentViewSet(ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    queryset = Document.objects.filter(id=0)
    serializer_class = DocumentSerializer


@api_view(["POST"],)
@permission_classes([permissions.AllowAny],)
def set_token(request):

    id_token = request.data['id_token']
    defaults = {"notification_token": request.data['notification_token']}

    profile = Profile.objects.update_or_create(id_token=id_token, defaults=defaults)

    if (profile):
        return Response("criado/atualizado.")
    else:
        return Response("Falha ao criar/atualizar.")


@api_view(["POST"],)
@permission_classes([permissions.AllowAny],)
def set_document(request):

    id_token = request.data['id_token']
    defaults = {"notification_token": request.data['notification_token'], "document": request.data['document']}

    profile, created = Profile.objects.update_or_create(id_token=id_token, defaults=defaults)

    return Response(created)


@api_view(["POST"],)
@permission_classes([permissions.AllowAny],)
def get_token(request):

    sender_id = request.data['sender_id']

    for profile in Profile.objects.filter(id_token=sender_id):
        senderToken = profile.notification_token

    return Response(senderToken)


@api_view(["GET"],)
@permission_classes([permissions.AllowAny],)
def notification_token(request):


    notificationTokenArray = []

    for token in Profile.objects.all():
        notificationTokenArray.append(token.notification_token)

    return Response(notificationTokenArray)


@api_view(["POST"],)
@permission_classes([permissions.AllowAny],)
def get_notification_token(request):

    idTokenArray = request.data['token_array']

    notificationTokenArray = []

    for token in idTokenArray:
        for tk in Profile.objects.filter(id_token=token):
            notificationTokenArray.append(tk.notification_token)

    return Response(notificationTokenArray)


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
