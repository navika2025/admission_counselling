from django.shortcuts import render
from common.models import HomePage, Banners, WhoWeAreSection, WhyChooseUsSection
from ytdata.models import Video
from common.models import Page


def index(request):
    page = Page.objects.get(slug = 'home-page')
    home_page = HomePage.objects.select_related("why_choose_us").prefetch_related("banners","who_we_are").first()

    featured_video = Video.objects.filter(show_on_homepage = True)
    context = {
        "page": page,
        "banners" : home_page.banners.first(),
        "why_choose_us" : home_page.why_choose_us,       
        "who_we_are" : home_page.who_we_are.all(),
        "featured" : featured_video
    }
    return render(request, "index.html" , context)