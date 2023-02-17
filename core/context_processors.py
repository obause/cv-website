from .models import Contact


def header_context(request):
    contact = Contact.objects.first()
    return {
        "contact": contact,
        "name": contact.full_name(),
        "social_media": contact.social_media.all(),

    }
