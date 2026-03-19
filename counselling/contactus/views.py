from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from contactus.models import ContactPage
from contactus.forms import ContactForm


def contact_page_view(request):
    contact_page = get_object_or_404(ContactPage, is_active=True)
    faq = contact_page.faqs.filter(is_active=True)

    context = {
        "contact": contact_page,
        "faqs": faq,
        "form": ContactForm(),
    }

    return render(request, "contactus.html", context)


@require_POST
def contact_form_ajax(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        inquiry = form.save()

        return JsonResponse({
            "success": True,
            "message": "Your message has been sent successfully!",
            "data": {
                "name": inquiry.name,
                "email": inquiry.email,
            }
        })

    return JsonResponse({"errors": form.errors})
