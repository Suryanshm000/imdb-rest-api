from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV, 
                                 ReviewList, ReviewDetail, ReviewCreate, 
                                 StreamPlatformVS, WatchListGV, UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('user-reviews/', UserReview.as_view(), name='user-review-list'),
    path('list2/', WatchListGV.as_view(), name='movie-list-filter'),
]
