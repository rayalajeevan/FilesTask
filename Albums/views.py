from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mixins import Mixins
from .serialiazer import *
# Create your views here.
class PostActivity(APIView,Mixins):

    def post(self,request,*args,**kwrgs):
        try:
            jsonObj=self.isValidJson(required_fields=["audioFileType","audioFileMetadata"])
            if jsonObj:
                if isinstance(jsonObj.get("audioFileMetadata"),dict):
                    if jsonObj.get("audioFileType")=="song":
                        serobj=SongSerializer(data=jsonObj.get("audioFileMetadata"),context={"save":True})
                    elif jsonObj.get("audioFileType")=="podcast":
                        serobj=PodcastSerializer(data=jsonObj.get("audioFileMetadata"),context={"save":True})
                    elif jsonObj.get("audioFileType")=="audiobook":
                        serobj=AudioBookSerializer(data=jsonObj.get("audioFileMetadata"),context={"save":True})
                    else:
                        return Response({"status":"FAILED","description":"please send valid audioFileType"},status=status.HTTP_400_BAD_REQUEST)
                    if serobj.is_valid():
                        serobj.save()
                        return Response({"status":"SUCCESS","data":serobj.data},status=status.HTTP_200_OK)
                    return Response({"status":"FAILED","description":serobj.errors},status=status.HTTP_400_BAD_REQUEST)
                return Response({"status":"FAILED","description":"audioFileMetadata must be a dictionary"},status=status.HTTP_400_BAD_REQUEST)
            return Response({"status":"FAILED","description":self.mixinErrors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({"status":"INTERNAL SERVER ERROR","description":str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteActivity(APIView,Mixins):
    def get_object(self,audioFileType,audioFileID):
        try:
            if audioFileType=="song":
                return Song.objects.get(song_id=audioFileID)
            elif audioFileType=="podcast":
                return Podcast.objects.get(podcast_id=audioFileID)
            elif audioFileType=="audiobook":
                return AudioBook.objects.get(audio_book_id=audioFileID)
            return {"error":"Invalid filetype"}
        except (Song.DoesNotExist,Podcast.DoesNotExist,AudioBook.DoesNotExist) as exc:
            return {"error":"Object not found"}
    def delete(self,request,audioFileType,audioFileID,*args,**kwrgs):
        try:
            activityObj=self.get_object(audioFileType,audioFileID)
            if not isinstance(activityObj,dict):
                activityObj.delete()
                return Response({"status":"SUCCESS"},status=status.HTTP_200_OK)
            return Response({"status":"FAILED","description":activityObj.get("error")},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({"status":"INTERNAL SERVER ERROR","description":str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class UpdateActivity(DeleteActivity):
    def put(self,request,audioFileType,audioFileID,*args,**kwrgs):
        try:
            jsonObj=self.isValidJson(required_fields=["audioFileType","audioFileMetadata"])
            if jsonObj:
                jsonObj=jsonObj.get("audioFileMetadata")
                activityObj=self.get_object(audioFileType,audioFileID)
                if not isinstance(activityObj,dict):
                    if audioFileType=="song":
                        serobj=SongSerializer(activityObj,jsonObj,partial=True)
                    elif audioFileType=="podcast":
                        serobj=PodcastSerializer(activityObj,jsonObj,partial=True)
                    elif audioFileType=="audiobook":
                        serobj=AudioBookSerializer(activityObj,jsonObj,partial=True)
                    if serobj.is_valid():
                        serobj.save()
                        return Response({"status":"SUCCESS","data":serobj.data},status=status.HTTP_200_OK)
                    return Response({"status":"FAILED","description":serobj.errors},status=status.HTTP_400_BAD_REQUEST)
                return Response({"status":"FAILED","description":activityObj.get("error")},status=status.HTTP_400_BAD_REQUEST)
            return Response({"status":"FAILED","description":self.mixinErrors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({"status":"INTERNAL SERVER ERROR","description":str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetActivity(DeleteActivity):
    def get_all_objects(self,audioFileType):
        if audioFileType=="song":
            return Song.objects.all()
        elif audioFileType=="podcast":
            return Podcast.objects.all()
        elif audioFileType=="audiobook":
            return AudioBook.objects.all()
        return {"error":"Invalid filetype"}

    def get(self,request,audioFileType,audioFileID=None,*args,**kwrgs):
        try:
            many=False
            if not audioFileID:
                activityObj=self.get_all_objects(audioFileType)
                many=True
            else:
                activityObj=self.get_object(audioFileType,audioFileID)
            if not isinstance(activityObj,dict):
                if audioFileType=="song":
                    serobj=SongSerializer(activityObj,many=many)
                elif audioFileType=="podcast":
                    serobj=PodcastSerializer(activityObj,many=many)
                elif audioFileType=="audiobook":
                    serobj=AudioBookSerializer(activityObj,many=many)
                return Response({"status":"SUCCESS","data":serobj.data},status=status.HTTP_200_OK)
            return Response({"status":"FAILED","description":activityObj.get("error")},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({"status":"INTERNAL SERVER ERROR","description":str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)