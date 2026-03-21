from django.shortcuts import render, get_object_or_404

from courses.models import CoursesPage

from common.models import Page



def courses(request):
    courses_page = CoursesPage.objects.first()

    context = {
        "page": courses_page.page,
        "courses_page": courses_page,
    }
    return render(request, "courses.html", context)