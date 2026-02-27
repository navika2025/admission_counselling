from django.shortcuts import render



def testimonials(request):
    return render(request, "testimonial.html")