from django.db import models

from counselling.models import BaseModel

from common.models import Page



class TestimonialPage(BaseModel):
    page = models.OneToOneField(
        "common.Page",
        on_delete=models.CASCADE,
        related_name="testimonial_page"
    )


    class Meta:
        verbose_name = "Testimonial Page"


    def __str__(self):
        return f"Testimonial Page"


class Testimonial(BaseModel):
    testimonial_page = models.ForeignKey(
        TestimonialPage,
        on_delete=models.CASCADE,
        related_name="testimonials"
    )
    name = models.CharField(
        max_length=100, 
        verbose_name="Student Name"
    )
    course_college = models.CharField(
        max_length=200, 
        verbose_name="Cousre and College name",
        help_text="B.Tech CSE, IIT Bombay"
    )
    batch = models.CharField(
        max_length=50, 
        verbose_name="Batch"
    )
    image = models.ImageField(
        upload_to="testimonials/photo/",
        blank=True, null=True,
        verbose_name="Student Photo"
    )
    review = models.TextField(
        verbose_name="Review Text"
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        verbose_name="Rating (1–5)",
        help_text="Student rating out of 5"
    )
    order = models.PositiveIntegerField(
        default=0
    )
    is_featured = models.BooleanField(
        default=False
    )


    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ["order"]


    def __str__(self):
        return f"{self.name} ({self.course_college})"