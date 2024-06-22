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


@api_view(['GET'])
def getNews(request):
    ctgList = newsAndHighlight.objects.all()
    ctgList = serializer.newsSerializer(ctgList, many = True)
    return Response(ctgList.data)

@api_view(['POST'])
def sendMsg(request):
    s = serializer.contactSerializer(data = request.data)
    if(s.is_valid()):
        s.save()
        return Response('message sent succesfully')
    else:
        return Response('error in sent data')


@api_view(['GET'])
def getGalleryAll(request):
    glList = galleryImages.objects.all()
    glList = serializer.gallerySerializer(glList, many=True)
    return Response(glList.data)


@api_view(['GET'])
def getGalleryHome(request):
    glList = galleryImages.objects.filter(show_on_homepage=True)
    glList = serializer.gallerySerializer(glList, many=True)
    return Response(glList.data)