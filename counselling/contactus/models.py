from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from counselling.models import BaseModel

from common.models import Page



class ContactPage(BaseModel):
    page = models.OneToOneField(
        "common.Page",
        on_delete=models.CASCADE,
        related_name="contact_page"
    )
    address = models.TextField(
        blank=True, null=True
    )
    support_email_1 = models.EmailField(
        blank=True, null=True
    )
    support_email_2 = models.EmailField(
        blank=True, null=True
    )
    support_phone_1 = models.CharField(
        max_length=20, 
        blank=True, null=True
    )
    support_phone_2 = models.CharField(
        max_length=20, 
        blank=True, null=True
    )
    map_embed_url = models.URLField(
        blank=True, null=True
    )


    class Meta:
        verbose_name = "Contact Page"


    def __str__(self):
        return f"Contact Page"
    

class ContactInquiry(BaseModel):

    class InterestChoices(models.TextChoices):
        GENERAL = "general", _("General Inquiry")
        SUPPORT = "support", _("Support")
        SALES = "sales", _("Sales")
        PARTNERSHIP = "partnership", _("Partnership")
        CAREERS = "careers", _("Careers")

    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Enter a valid phone number (up to 15 digits)."
    )

    name = models.CharField(
        max_length=100
    )
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_validator],
    )
    interest = models.CharField(
        max_length=20,
        choices=InterestChoices.choices,
        default=InterestChoices.GENERAL
    )
    message = models.TextField()
    is_resolved = models.BooleanField(
        default=False
    )


    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ["-created_at"]


    def __str__(self):
        return f"{self.name} - {self.interest}"
    


class FAQ(BaseModel):
    contact_page = models.ForeignKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="faqs"
    )

    question = models.TextField()
    answer = models.TextField()
    order = models.PositiveIntegerField(
        default=0
    )


    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["order"]


    def __str__(self):
        return self.question
