from rest_framework.test import APITestCase, APIClient
from user_profile.apps import UserProfileConfig
from django.apps import apps
from django.test import TestCase
from rest_framework import status


class ProfileTests(APITestCase):

    def testing_post(client):
        client = APIClient()
        client.post('/set_token/',
                    {'id_token': 1, 'notification_token': 'new notification token'}, format='json')

    def testing_get(client):
        client = APIClient()
        client.get('/notification_token/')

    def testing_patch(client):
        client = APIClient()
        client.patch('/set_token/', {'notification_token': 'notification test'})

    def testing_post_notification_token(client):
        client = APIClient()
        client.post('/get_notification_token/', {'id_token': '1'}, format='json')

    def testing_current_user(client):
        client = APIClient()
        client.get('/current_user/')


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
