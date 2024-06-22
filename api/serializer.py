from rest_framework import serializers
from .models import memberProfile, category , contactMsg , newsAndHighlight
from .models import *


class memberProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = memberProfile
        fields = '__all__'

class memberProfileSmallSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = memberProfile
        fields = ['user', 'first_name', 'last_name', 'photo', 'playing_in', 'gender', 'achievements', 'school_college']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactMsg
        fields = '__all__'

class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsAndHighlight
        fields = '__all__'