from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from user_profile.views import ProfileViewSet, DocumentViewSet, get_token
from user_profile.views import set_token, get_notification_token, notification_token, set_document
from rest_framework_jwt.views import obtain_jwt_token
from user_profile.views import current_user, UserList
from django.conf.urls.static import static
from django.conf import settings


router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^notification_token/$', notification_token),
    url(r'^get_token/$', get_token),
    url(r'^set_token/$', set_token),
    url(r'^set_document/$', set_document),
    url(r'^get_notification_token/$', get_notification_token),
    path('token-auth/', obtain_jwt_token),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
