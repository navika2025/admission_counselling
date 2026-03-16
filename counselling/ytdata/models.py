from django.db import models

from counselling.models import BaseModel

from common.models import Page

# source .venv/Scripts/activate

class YouTubePage(BaseModel):
    page = models.OneToOneField(
        "common.Page",
        on_delete=models.CASCADE,
        related_name="video_page"
    )


    class Meta:
        verbose_name = "YouTube Page"


    def __str__(self):
        return f"YouTube Page"
    

class VideoStatistic(BaseModel):
    video_page = models.ForeignKey(
        YouTubePage,
        on_delete=models.CASCADE,
        related_name="statistics"
    )
    label = models.CharField(
        max_length=100,
        help_text = "Videos, Views"
    )
    value = models.CharField(
        max_length=50,
        help_text="150+, 2M+"
    )
    icon = models.ImageField(
        upload_to="yt/staticon"
    )
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["order"]
        verbose_name = "Video Statistic"
        verbose_name_plural = "Video Statistics"


    def __str__(self):
        return f"{self.label}: {self.value}"



class VideoCategory(BaseModel):
    video_page = models.ForeignKey(
        YouTubePage,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(
        max_length=100,
        help_text="NEET/JEE/LLB"
    )
    slug = models.SlugField(
        unique=True
    )
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["order"]
        verbose_name = "Video Category"
        verbose_name_plural = "Video Categories"


    def __str__(self):
        return self.name


class Video(BaseModel):
    category = models.ForeignKey(
        VideoCategory,
        on_delete=models.CASCADE,
        related_name="videos"
    )
    title = models.CharField(
        max_length=250
    )
    description = models.TextField()
    youtube_url = models.URLField(
        help_text="Paste YouTube video URL"
    )
    thumbnail = models.ImageField(
        upload_to="yt/thumbnails/",
        blank=True, null=True
    )
    duration = models.CharField(
        max_length=10,
        help_text="Example: 15:30"
    )
    views = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="125K views"
    )
    is_featured = models.BooleanField(
        default=False
    )
    order = models.PositiveIntegerField(
        default=0
    )
    
    show_on_homepage = models.BooleanField(
        default=False
    )



    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Video"
        verbose_name_plural = "Videos"


    def __str__(self):
        return f"{self.title} {self.category.name}"
    

class Playlist(BaseModel):
    video_page = models.ForeignKey(
        YouTubePage,
        on_delete=models.CASCADE,
        related_name="playlists"
    )
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    playlist_url = models.URLField()


    order = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ["order"]
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"


    def __str__(self):
        return self.title
    