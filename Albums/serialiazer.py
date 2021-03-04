from .models import *
from rest_framework import serializers
from .mixins import *

class SongSerializer(Mixins,serializers.ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"
    
    def __init__(self,*args,**kwrgs):
        super(SongSerializer,self).__init__(*args,**kwrgs)
        if self.context.get('fields')!=None:
            for key in list(self.fields.keys()):
                if key not in self.context.get('fields'):
                    self.fields.pop(key)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for  key,value in validated_data.items():
            if key in  instance.__dict__.keys():
                if key!="uploaded_on":
                    instance.__dict__[key]=value
        instance.save()
        return instance

class PodcastSerializer(Mixins,serializers.ModelSerializer):
    class Meta:
        model=Podcast
        fields="__all__"
    
    def __init__(self,*args,**kwrgs):
        super(PodcastSerializer,self).__init__(*args,**kwrgs)
        if self.context.get('fields')!=None:
            for key in list(self.fields.keys()):
                if key not in self.context.get('fields'):
                    self.fields.pop(key)

    def create(self, validated_data):
        return Podcast.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for  key,value in validated_data.items():
            if key in  instance.__dict__.keys():
                if key!="uploaded_on":
                    instance.__dict__[key]=value
        instance.save()
        return instance

class AudioBookSerializer(Mixins,serializers.ModelSerializer,):
    class Meta:
        model=AudioBook
        fields="__all__"
    
    def __init__(self,*args,**kwrgs):
        super(AudioBookSerializer,self).__init__(*args,**kwrgs)
        if self.context.get('fields')!=None:
            for key in list(self.fields.keys()):
                if key not in self.context.get('fields'):
                    self.fields.pop(key)

    def create(self, validated_data):
        return AudioBook.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for  key,value in validated_data.items():
            if key in  instance.__dict__.keys():
                if key!="uploaded_on":
                    instance.__dict__[key]=value
        instance.save()
        return instance