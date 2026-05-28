from django.shortcuts import render, get_object_or_404
from .models import AboutUsPage

from django.shortcuts import render
from common.models import Page

def about_us(request):
    page = Page.objects.get(slug='about-us')
    # about_page = get_object_or_404(AboutUsPage, is_active = True)
    about_page = AboutUsPage.objects.first()
    story_sec = about_page.story_section
    core_values = about_page.core_values.all()
    team_members = about_page.team_members.all()
    context = {
        "page" : page,
        "about": about_page,
        "story_section": story_sec,
        "core_values": core_values,
        "team_members": team_members,
    }
    return render(request, "about_us.html",context)