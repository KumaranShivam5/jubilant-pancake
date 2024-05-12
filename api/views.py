from django.shortcuts import render

# Create your views here.

from .models import *

from rest_framework.decorators import api_view

from rest_framework.response import Response 


# class 


from django.contrib.auth.models import User 
from django.db.utils import IntegrityError 
from .import serializer

@api_view(['GET'])
def getMemberList(request):
    memberList = memberProfile.objects.all()
    memberList = serializer.memberProfileSmallSerializer(memberList, many=True)
    return Response(memberList.data)


@api_view(['GET'])
def getCategoryList(request):
    ctgList = category.objects.all()
    ctgList = serializer.CategorySerializer(ctgList, many = True)
    return Response(ctgList.data)
