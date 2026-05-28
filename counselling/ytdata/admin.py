from django.contrib import admin
from ytdata.models import VideoStatistic, VideoCategory, Playlist, YouTubePage, Video
# Register your models here.

class VideoStatisticInline(admin.StackedInline):
    model = VideoStatistic
    extra = 1
    
class VideoCategoryInline(admin.StackedInline):
    model = VideoCategory
    extra = 1
    
class PlaylistInline(admin.StackedInline):
    model = Playlist
    extra = 1
    
class VideoInline(admin.StackedInline):
    model = Video
    extra = 1
    
@admin.register(YouTubePage)
class YouTubePageAdmin(admin.ModelAdmin):
    list_display = ("page","created_at",)
    inlines = [
        VideoStatisticInline,
        VideoCategoryInline,
        PlaylistInline,
    ]

@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","video_page","order")
    list_filter = ("video_page",)  
    inlines = [
        VideoInline
    ]