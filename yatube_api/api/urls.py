from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, GroupViewSet, PostViewSet, FollowsViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')
router.register('follow', FollowsViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
