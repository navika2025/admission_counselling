from django.urls import path
from courses.views import courses

urlpatterns = [
    path("courses/", courses, name="courses"),
]