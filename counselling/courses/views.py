from django.shortcuts import render
from courses.models import CoursesPage, ExamCategory, Course, TopCollege, NeedHelpSection
from common.models import Page


def courses(request):
    page = Page.objects.get(slug = 'courses')
    courses_page = CoursesPage.objects.select_related("guidance_section").prefetch_related("exam_categories__courses","exam_categories__top_colleges").first()
    
    exam_category = request.GET.get("exam_category")
    courses = Course.objects.all()
    top_colleges = TopCollege.objects.all()

    # if exam_category:
    #     selected_category = courses_page.exam_categories.get(id = exam_category)
             
    # else:
    #     selected_category = courses_page.exam_categories.first()
        

    context = {
        "page" : page,
        "exam_category" : courses_page.exam_categories.all(),
        "courses" : courses,
        "top_colleges" : top_colleges,
        "guidance" : courses_page.guidance_section,   
    }
    return render(request, "courses.html" , context)
