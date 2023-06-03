from django.urls import path
from watchlist_app.api.views import *
urlpatterns = [
    path('list/',WatchListAV.as_view(),name='watch-list' ),
    path('watch/<int:pk>',WatchlistDetailAV.as_view(),name='watchlist-detail' ),
    path('stream/',StreamplatformAV.as_view(),name='stream-list'),
    path('stream/<int:pk>',StreamplatformDetailAV.as_view(),name='stream-Detail'),
    # path('review',ReviewList.as_view(),name="review-list"),
    # path('review/<int:pk>',ReviewDetail.as_view(),name="review-detail"),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name="review-create"),
    path('stream/<int:pk>/review',Reviewlist.as_view(),name="review-list"),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name="review-detail"),



]
