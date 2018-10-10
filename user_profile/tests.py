from rest_framework import status
from .models import Profile
from .views import ProfileViewSet
from rest_framework.test import APITestCase, APIClient, APIRequestFactory


class ProfileTests(APITestCase):
    def test_create_profile(self):
        url = '/profiles/'
        data = {'id_token': 'new id token', 'notification_token': 'new notification token'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().id_token, 'new id token')
        self.assertEqual(Profile.objects.get().notification_token, 'new notification token')

    def test_view_set(self):
        request = APIRequestFactory().get('')
        profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})
        profile = Profile.objects.create(id_token='id token', notification_token='notification token')
        response = profile_detail(request, pk=profile.pk)
        self.assertEqual(response.status_code, 200)

    def testing_post(client):
        client = APIClient()
        client.post('/set_token/',
                    {'id_token': 'new id token', 'notification_token': 'new notification token'}, format='json')

    def testing_get(client):
        client = APIClient()
        client.get('/notification_token/')

    def testing_patch(client):
        client = APIClient()
        client.patch('/set_token/', {'notification_token': 'notification test'})
