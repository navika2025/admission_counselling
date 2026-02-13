from django.db import models
from django.utils.text import slugify
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True        
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


class SEOModel(models.Model):
    meta_title = models.CharField(
        max_length=150, 
        blank=True, null=True
    )
    meta_description = models.TextField(
        blank=True, null=True
    )
    meta_keywords = models.CharField(
        max_length=250, 
        blank=True, null=True
    )

    class Meta:
        abstract = True