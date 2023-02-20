from django.shortcuts import render
from django.template import RequestContext

from .models import Contact, Interests, WorkExperience


def home(request):
    # contact = Contact.objects.first()

    return render(request, "core/main.html")


def about(request):
    context = {"interest_rows": []}
    all_interests = Interests.objects.all()
    # row = 0
    row_content = []
    for i, interest in enumerate(all_interests):
        print(i, interest)
        row_content.append(interest)
        if i % 2 == 1:
            context['interest_rows'].append(row_content)
            row_content = []
    if len(row_content) > 0:
        context['interest_rows'].append(row_content)

    fun_facts = Contact.objects.first().fun_facts.all()
    context['fun_facts'] = fun_facts

    return render(request, "core/about.html", context)


def resume(request):
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

    # Order skills by percentage in every category
    # for category in skills_by_category:
    #     skills_by_category[category]['skills'] = sorted(
    #         skills_by_category[category]['skills'],
    #         key=lambda x: (x is None, x.percentage),
    #         reverse=True
    #     )

    context = {
        "education_items": education_items,
        "work_experience_items": work_experience_items,
        "skills_by_category": skills_by_category,
        "certificates": certificates
    }

    print(skills_by_category)

    return render(request, "core/resume.html", context)


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
