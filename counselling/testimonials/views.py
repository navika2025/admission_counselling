from django.shortcuts import render, get_object_or_404
from testimonials.models import TestimonialPage
from common.models import Page


def testimonials(request):
    page = Page.objects.get(slug = 'testimonial')
    testimonial_page = get_object_or_404(TestimonialPage, is_active = True)
    testimonial = testimonial_page.testimonials.all()
    context = {
        "page": page,
        "testimonial_page" : testimonial_page,
        "testimonial": testimonial
    }
    return render(request, "testimonial.html" , context)