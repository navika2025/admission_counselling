from django.db import models

from counselling.models import BaseModel

from common.models import Page



class CoursesPage(BaseModel):
    page = models.OneToOneField(
        "common.Page",
        on_delete=models.CASCADE,
        related_name="courses_page"
    )

    class Meta:
        verbose_name = "Courses Page"


    def __str__(self):
        return f"Courses Page"


class ExamCategory(BaseModel):
    courses_page = models.ForeignKey(
        CoursesPage,
        on_delete=models.CASCADE,
        related_name="exam_categories"
    )
    title = models.CharField(
        max_length=150,
        help_text="NEET/JEE/LAW"
    )
    short_description = models.TextField(
        blank=True, null=True
    )
    icon = models.ImageField(
        upload_to="courses/examcategory",
        null=True, blank=True
    )
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["order"]
        verbose_name = "Exam Category"
        verbose_name_plural = "Exam Categories"


    def __str__(self):
        return self.title


class Course(BaseModel):
    exam_category = models.ForeignKey(
        ExamCategory,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    name = models.CharField(
        max_length=200,
        help_text="MBBS/BDS/BHMS"
    )
    duration = models.CharField(
        max_length=50
    )
    short_description = models.TextField()
    career_opportunities = models.TextField(
        help_text="Comma separated or paragraph format"
    )
    eligibility = models.TextField()
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["order"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"


    def __str__(self):
        return self.name


class TopCollege(BaseModel):

    class CollegeType(models.TextChoices):
        GOVERNMENT = "government", "Government"
        PRIVATE = "private", "Private"

    exam_category = models.ForeignKey(
        ExamCategory,
        on_delete=models.CASCADE,
        related_name="top_colleges"
    )
    name = models.CharField(
        max_length=200
    )
    college_type = models.CharField(
        max_length=20,
        choices=CollegeType.choices,
        default=CollegeType.GOVERNMENT
    )
    location = models.CharField(
        max_length=150,
        blank=True, null=True
    )
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        ordering = ["order"]
        verbose_name = "Top College"
        verbose_name_plural = "Top Colleges"


    def __str__(self):
        return self.name


class NeedHelpSection(BaseModel):
    courses_page = models.ForeignKey(
        CoursesPage,
        on_delete=models.CASCADE,
        related_name="guidance_section"
    )

    title = models.CharField(
        max_length=200,
    )
    description = models.CharField(
        max_length=250
    )
    icon = models.ImageField(
        upload_to="courses/needhelp",
        null=True, blank=True
    )


    class Meta:
        verbose_name = "Need Help Section"


    def __str__(self):
        return self.title
