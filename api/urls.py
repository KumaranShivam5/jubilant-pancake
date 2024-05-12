from django.urls import path 
from . import views 

urlpatterns = [
    path("member-list/", views.getMemberList),
    path("get-all-ctg/", views.getCategoryList),
]