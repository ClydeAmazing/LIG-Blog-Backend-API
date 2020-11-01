from django.urls import path, include
from api.models import Post, Comment
from api.viewsets import PostViewSet
from api.views import login, logout, register
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

router = routers.DefaultRouter(trailing_slash=False)
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<slug:slug>/comments', PostViewSet.as_view({'get': 'get_comments', 'post': 'post_comment'}), name='comments'),
    path('posts/<slug:slug>/comments/<int:pk>', PostViewSet.as_view({'get': 'get_comments'}), name='get_comment'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
] 