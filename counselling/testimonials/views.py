from django.shortcuts import render

from testimonials.models import TestimonialPage



def testimonials(request):
    testimonial_page = TestimonialPage.objects.prefetch_related("testimonials").first()
    featured = testimonial_page.testimonials.filter(is_featured=True).order_by("-id").first()
    testimonials = testimonial_page.testimonials.all()

    context = {
        "testimonial_page": testimonial_page,
        "testimonials": testimonials,
        "featured": featured,
    }

    return render(request, "testimonial.html", context)
    return render(request, "testimonial_dynamic.html", context)
