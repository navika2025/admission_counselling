from django.urls import path
from contactus.views import contact_page_view, contact_form_ajax

urlpatterns = [
    path("contact/", contact_page_view, name="contact"),
    path("submit/", contact_form_ajax, name="contact_ajax"),
]