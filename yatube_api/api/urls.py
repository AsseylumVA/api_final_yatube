from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, GroupViewSet, PostViewSet, FollowsViewSet


router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')
router.register('v1/follow', FollowsViewSet, basename='follows')

urlpatterns = [
    path('', include(router.urls)),
]
