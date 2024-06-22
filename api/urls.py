from django.urls import path
from . import views

urlpatterns = [
    path("member-list/", views.getMemberList),
    path("get-all-ctg/", views.getCategoryList),
    path('send-message/' , views.sendMsg),
    path('get-news/', views.getNews),
    path('get-gallery-home/', views.getGalleryHome),
    path('get-gallery-all/', views.getGalleryAll)
]