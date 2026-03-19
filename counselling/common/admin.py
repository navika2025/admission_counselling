from django.contrib import admin
from common.models import Page, Banners, WhoWeAreSection, WhyChooseUsSection, HomePage

class BannerInline(admin.TabularInline):
    model = Banners
    extra = 0
    
class WhoWeAreInline(admin.TabularInline):
    model = WhoWeAreSection
    extra = 0
    
class WhyChooseUsInline(admin.TabularInline):
    model = WhyChooseUsSection
    extra = 0
    

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("page", "created_at")
    inlines = [
        BannerInline,
        WhoWeAreInline,
        WhyChooseUsInline
    ]

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('meta_title', 'meta_description', 'meta_keywords')


