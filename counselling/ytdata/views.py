from django.shortcuts import render

from ytdata.models import YouTubePage, VideoStatistic, VideoCategory, Video, Playlist


def youtube(request):
    page_obj = YouTubePage.objects.prefetch_related(
        "statistics",
        "categories__videos",
        "playlists"
    ).first()

    videos = Video.objects.select_related("category").all()

    context = {
        "youtube_page": page_obj,
        "stats": page_obj.statistics.all(),
        "categories": page_obj.categories.all(),
        "videos": videos,
        "playlists": page_obj.playlists.all(),
    }

    # return render(request, "youtube.html", context)
    return render(request, "youtube_dynamic.html", context)