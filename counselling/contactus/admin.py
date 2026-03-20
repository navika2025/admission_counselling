from django.contrib import admin
from django.http import HttpRequest

from contactus.models import ContactPage, ContactInquiry, FAQ



# class FAQInline(admin.TabularInline):
#     model = FAQ
#     extra = 1
#     fields = ("question", "answer", "order", "is_active")
#     ordering = ("order",)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):

    list_display = ("page", "support_email_1", "support_phone_1", "is_active", "created_at")
    search_fields = ("page__title", "support_email_1", "support_phone_1")
    list_filter = ("is_active", "created_at")
    # inlines = [FAQInline]

    fieldsets = (
        ("Page Relation", {
            "fields": ("page",)
        }),
        ("Contact Details", {
            "fields": (
                "address",
                "map_embed_url",
            )
        }),
        ("Emails", {
            "fields": (
                "support_email_1",
                "support_email_2",
            )
        }),
        ("Phone Numbers", {
            "fields": (
                "support_phone_1",
                "support_phone_2",
            )
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
    )

    def has_add_permission(self, request):
        return False
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = ("question", "contact_page", "order", "is_active",)
    list_filter = ("contact_page", "is_active")
    search_fields = ("question", "answer")
    ordering = ("order",)
    autocomplete_fields = ("contact_page",)
    
    


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "phone_number", "interest", "is_resolved", "created_at",)
    list_filter = ("interest", "is_resolved", "created_at")
    search_fields = ("name", "email", "phone_number", "message",)
    readonly_fields = ("name", "email", "phone_number", "interest", "message", "created_at", "updated_at")
    list_editable = ("is_resolved",)
    ordering = ("-created_at",)

    fieldsets = (
        ("User Information", {
            "fields": (
                "name",
                "email",
                "phone_number",
            )
        }),
        ("Inquiry Details", {
            "fields": (
                "interest",
                "message",
            )
        }),
        ("Status", {
            "fields": ("is_resolved",)
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

