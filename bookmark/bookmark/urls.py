from django.urls import path

from bookmark.views import BookmarkCreate, BookmarkDelete, BookmarkUpdate, BookmarkDetail, BookmarkList

app_name = 'bookmark'

urlpatterns = [
    path('create/', BookmarkCreate.as_view(), name='create'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name='delete'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name='update'),
    path('deteil/<int:pk>', BookmarkDetail.as_view(), name='detail'),
    path('', BookmarkList.as_view(), name='list'),
]