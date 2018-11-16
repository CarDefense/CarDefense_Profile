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
from user_profile.views import ProfileViewSet, DocumentViewSet
from user_profile.views import set_token, get_notification_token, notification_token
from rest_framework_jwt.views import obtain_jwt_token
from user_profile.views import current_user, UserList
from django.conf.urls.static import static
from django.conf import settings


router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^notification_token/$', notification_token),
    url(r'^set_token/$', set_token),
    url(r'^get_notification_token/$', get_notification_token),
    path('token-auth/', obtain_jwt_token),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
