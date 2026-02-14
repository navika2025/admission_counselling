from django.contrib import admin
from common.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('meta_title', 'meta_description', 'meta_keywords')
