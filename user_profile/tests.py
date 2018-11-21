from rest_framework.test import APITestCase, APIClient
from user_profile.apps import UserProfileConfig
from django.apps import apps
from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response


class ProfileTests(APITestCase):

    def testing_set_token(self):
        data = {'id_token': 1, 'notification_token': 'new notification token'}
        self.client.post('/set_token/', data=data)

    def testing_set_token_wrong(self):
        data = {'id_token': 0, 'notification_token': ''}
        self.client.post('/set_token/', data=data)

    def testing_get(self):
        self.client.get('/notification_token/')

    def testing_patch(self):
        data = {'notification_token': 'notification test'}
        self.client.patch('/set_token/', data=data)

    def testing_post_notification_token(self):
        data = {'token_array': 1}
        self.client.post('/get_notification_token/', data=data)

    def testing_set_document(self):
        data = {'id_token': 1, "notification_token": '', 'document': ''}
        self.client.post('/set_document/', data=data)

    def testing_current_user(self):
        user = {'username': 'biel', 'password': 'asjasajsnasaj'}
        serializer = UserSerializer(user)
        response = Response(serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def testing_get_token(self):
    #     data = {'sender_id': 1, 'notification_token': 'abc'}
    #     self.client.post('/profiles/', data=data)
    #     key = data["sender_id"]
    #     data1 = {'sender_id': key}
    #     self.client.post('/get_token/', data=data1)


class UserConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(UserProfileConfig.name, 'user_profile')
        self.assertEqual(apps.get_app_config('user_profile').name, 'user_profile')


class UserListTest(APITestCase):

    def testing_post(self):
        url = '/users/'
        serializer = '123'
        response = self.client.post(url, serializer, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BaseTestCase(TestCase):

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.username = 'test user'
        self.password = 'testing'
        user = User.objects.create_user(username=self.username, password=self.password)
        user.save()
        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.url = '/token-auth/'


class ObtainJSONWebTokenTests(BaseTestCase):

    def test_jwt_login_json(self):
        client = APIClient(enforce_csrf_checks=True)

        response = client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_jwt_login_json_incomplete_creds(self):
        client = APIClient(enforce_csrf_checks=True)

        self.data = {
            'username': self.username
        }
        response = client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
