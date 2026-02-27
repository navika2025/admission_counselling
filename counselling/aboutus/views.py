from django.shortcuts import render
from .models import AboutUsPage

from django.shortcuts import render

def about_us(request):
    about_page = AboutUsPage.objects.first()
    context = {
        "about_page": about_page,
    }
    return render(request, "about_us.html",context)