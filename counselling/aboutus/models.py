from django.db import models

from counselling.common.models import Page
from counselling.counselling.models import BaseModel

# Create your models here.
class AboutUsPage(BaseModel):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="about_page"
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return f"About Extension - {self.page.title}"


class OurStorySection(BaseModel):
    about_page = models.OneToOneField(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="story_section"
    )

    story_text = models.TextField(
        null=True, blank=True,
        verbose_name="Story Description"
    )
    vision_text = models.TextField(
        blank=True, null=True,
        verbose_name="Vision Description"
    )
    mission_text = models.TextField(
        blank=True, null=True,
        verbose_name="Mission Description"
    )

    def __str__(self):
        return f"Story - {self.about_page.page.title}"


class OurCoreValue(BaseModel):
    about_page = models.ForeignKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="core_values"
    )

    title = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name="Value Title"
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Value Text"
    )
    icon = models.ImageField(
        upload_to="about/core_values/",
        blank=True, null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class OurTeamMember(BaseModel):
    about_page = models.ForeignKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="team_members"
    )
    name = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name="Member Name"
    )
    image = models.ImageField(
        upload_to="about/team/",
        blank=True, null=True,
        verbose_name="Member Image"
    )
    designation = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name="Member Designation"
    )
    domain = models.CharField(
        max_length=150,
        null=True, blank=True,
        verbose_name="Member Domain"
    )
    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.designation}"
    
