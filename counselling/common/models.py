from django.db import models
from django.utils.text import slugify

from counselling.models import BaseModel, SEOModel


class Page(BaseModel, SEOModel):
    title = models.CharField(
        max_length=150
    )
    slug = models.SlugField(
        unique=True,                     
        blank=True, null=True
    )
    banner_image = models.ImageField(
        upload_to="pages/banners/",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class HomePage(BaseModel):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="home_page"
    )

    class Meta:
        verbose_name = "Home Page"

    def __str__(self):
        return "Home Page"
    

class Banners(BaseModel):
    home_page = models.ForeignKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="banners"
    )
    button_text = models.CharField(
        max_length=50, 
        null=True, blank=True, 
        verbose_name="Button Text"
    )
    button_url = models.URLField(
        blank=True, null=True,
        verbose_name="Banner Url", 
    )
    desktop_image = models.ImageField(
        null=True, blank=True,
        upload_to = "banner/images",
        verbose_name="Banner Image"
    )
    alt_text = models.CharField(
        verbose_name="Alt Text",
        max_length=150,
        blank=True, null=True,
    )
    desktop_video = models.FileField(
        null=True, blank=True,
        upload_to = "banners/videos",
        verbose_name="Banner Video"
    )
    heading = models.CharField(
        max_length=30, 
        blank=True, null=True,
        verbose_name="Banner Heading", 
    )
    banner_text = models.CharField(
        blank=True, null=True,
        verbose_name="Banner Text", 
    )
    
    def __str__(self):
        return self.heading or self.banner_text
    
    class Meta:
        verbose_name = "Banner"

    
class WhoWeAreSection(BaseModel):
    home_page = models.ForeignKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="who_we_are"
    )
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    icon = models.ImageField(
        upload_to="home/features/",
        blank=True, null=True
    )
    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Who We Are Section"

    def __str__(self):
        return f"Who We Are Section - {self.title}"
    
    
class WhyChooseUsSection(BaseModel):
    home_page = models.OneToOneField(
        HomePage,
        on_delete=models.CASCADE,
        related_name="why_choose_us"
    )
    image = models.ImageField(
        upload_to="home/features/",
        blank=True, null=True
    )
    text = models.TextField(
    )
    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Why Choose Us Section"

    def __str__(self):
        return "Why Choose Us Section"