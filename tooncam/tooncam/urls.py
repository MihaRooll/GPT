from django.contrib import admin
from django.urls import path

from apps.output import video_feed

urlpatterns = [
    path("admin/", admin.site.urls),
    path("video/", video_feed, name="video-feed"),
]
