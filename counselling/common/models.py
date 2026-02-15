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