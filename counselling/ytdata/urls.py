from django.urls import path
from ytdata.views import youtube

urlpatterns = [
    path("youtube/", youtube, name="youtube"),
]