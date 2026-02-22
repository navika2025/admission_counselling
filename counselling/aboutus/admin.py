from django.contrib import admin

from aboutus.models import AboutUsPage, OurStorySection, OurCoreValue, OurTeamMember


class OurStorySectionInline(admin.StackedInline):
    model = OurStorySection
    extra = 0


class OurCoreValueInline(admin.TabularInline):
    model = OurCoreValue
    extra = 1


class OurTeamMemberInline(admin.TabularInline):
    model = OurTeamMember
    extra = 1


@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ("page", "created_at")
    inlines = [
        OurStorySectionInline,
        OurCoreValueInline,
        OurTeamMemberInline,
    ]

