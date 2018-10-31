"""api_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from user_profile.views import ProfileViewSet, notification_token
from user_profile.views import set_token, get_notification_token
# from login_profile.views import create_user

from rest_framework.routers import DefaultRouter
from login_profile import views


router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)

# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
# router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^notification_token/$', notification_token),
    url(r'^set_token/$', set_token),
    url(r'^get_notification_token/$', get_notification_token),
    # url(r'^create_user', create_user),
]
