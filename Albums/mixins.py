import json
import datetime
from rest_framework import serializers
class Mixins:
    def isValidJson(self,required_fields=None):
        try:
            self.mixinErrors=list()
            if hasattr(self,"request"):
                json_data=json.loads(self.request.body)
                if required_fields:
                    self.mixinErrors=[x for x in list(map(lambda x:{x:[{"description":"this field is required"}]} if x not in json_data.keys() else None,required_fields)) if x is not None]
                return json_data if len(self.mixinErrors)==0 else None
            raise Exception("This Mixin Works only Rest Frame work Class based views")
        except json.decoder.JSONDecodeError as exc:
            self.mixinErrors=[{"json":[{"description":"Invalid Json Data"}]}]
            return None
    
    def checkValidDateFormat(self,value):
        try:
            if datetime.datetime.now()<= datetime.datetime.strptime(value.strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")+datetime.timedelta(minutes=1):
                return value
            return {"error":"Uploaded time canonot be in past"}
        except ValueError as exc:
            return  {"error":"Invalid Date format"}
    def validate(self,data):
        if data.get("duration")!=None and data.get("duration")<1:
            raise serializers.ValidationError("duration must be postive integer")
        if self.context.get("save"):
            if data.get("uploaded_on")!=None:
                dateObj=self.checkValidDateFormat(data.get("uploaded_on"))
                if not isinstance(dateObj,dict):
                    return data
                raise serializers.ValidationError(dateObj.get("error"))
        return data
