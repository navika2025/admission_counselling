from django.contrib import admin
from testimonials.models import TestimonialPage, Testimonial

# Register your models here.
class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 1

@admin.register(TestimonialPage)
class TestimonialPageAdmin(admin.ModelAdmin):
    list_display = ("page", "created_at")
    inlines = [
        TestimonialInline
    ]