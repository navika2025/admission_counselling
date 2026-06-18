from django.shortcuts import render
from .models import YouTubePage, Video
from common.models import Page


def youtube(request):
    page = Page.objects.get(slug = 'youtube')
    video_page = YouTubePage.objects.prefetch_related("statistics","categories__videos","playlists").first()
    
    if not video_page:
        return render(request, "youtube.html", {})    
    
    # Get category from URL
    
    category_slug = request.GET.get("category")
    
    if category_slug:
        filtered_videos = Video.objects.filter(
            category__slug = category_slug,
            category__video_page = video_page
        )
    
    else:
        filtered_videos = Video.objects.filter(
            category__video_page = video_page
        )
        
        
    featured = filtered_videos.filter(is_featured = True).order_by("-id").first()    
    
    context = {
        "page" : page,
        "video": video_page,
        "video_stats": video_page.statistics.all(),
        "categories": video_page.categories.all(),
        "playlists": video_page.playlists.all(),
        "filtered_videos": filtered_videos,
        "featured": featured,
    }
    return render(request, "youtube.html",context)
