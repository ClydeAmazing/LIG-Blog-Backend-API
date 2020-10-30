from django.urls import path, include
from api.models import Post, Comment
from api.viewsets import PostViewSet
from api.views import login, logout
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
] 