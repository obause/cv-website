from .models import Contact
from django.conf import settings

CONTACT_PK = settings.CONTACT_PK


def header_context(request):
    contact = Contact.objects.get(pk=CONTACT_PK)
    return {
        "contact": contact,
        "name": contact.full_name(),
        "social_media": contact.social_media.all(),
    }
