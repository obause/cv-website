from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from core.models import Contact

import pdfkit
from wsgiref.util import FileWrapper


# Create your views here.
def resume_pdf(request):
    contact = Contact.objects.first()
    education_items = contact.education.all().order_by("-start_date")
    work_experience_items = contact.experience.all().order_by("-start_date")
    certificates = contact.certificates.all()
    skills = contact.skills.all()

    skills_by_category = {}
    for skill in skills:
        if skill.category.name not in skills_by_category:
            skills_by_category[skill.category.name] = {"is_percentage": skill.category.is_percentage, "skills": []}
        skills_by_category[skill.category.name]['skills'].append(skill)

    context = {
        "education_items": education_items,
        "work_experience_items": work_experience_items,
        "skills_by_category": skills_by_category,
        "certificates": certificates
    }

    return render(request, "pdfgen/resume_light.html", context)

# def resume_pdf(request):
#     contact = Contact.objects.first()
#     html = loader.render_to_string('pdfgen/resume_light.html', {'contact': contact})
#     # options={
#     #    'page-size': 'Letter',
#     #    'encoding' : 'UTF-8',
#     # }

#     print(html)

#     config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
#     pdf = pdfkit.from_string(html, False, configuration=config)
#     print(f"PDF: {pdf}")
#     # pdf = pdfkit.from_string("<h1>Test</h1>", "test.pdf", configuration=config)
#     # response = HttpResponse(pdf, content_type='application/pdf')
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment;filename="cv.pdf"'
#     return response
