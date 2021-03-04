
from django.urls import path
from .views import *
urlpatterns = [
    path("create/activity",PostActivity.as_view(),name="PostActivity"),
    path("delete/activity/<str:audioFileType>/<int:audioFileID>/",DeleteActivity.as_view(),name="DeleteActivity"),
    path("update/activity/<str:audioFileType>/<int:audioFileID>/",UpdateActivity.as_view(),name="UpdateActivity"),
    path("get/activity/<str:audioFileType>/",GetActivity.as_view(),name="GetActivityForAll",),
    path("get/activity/<str:audioFileType>/<int:audioFileID>/",GetActivity.as_view(),name="GetActivityIndividual",),
]
