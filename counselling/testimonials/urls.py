from django.urls import path
from testimonials.views import testimonials

urlpatterns = [
    path("testimonials/", testimonials, name="testimonials"),
]