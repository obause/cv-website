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
    print(context)
    return render(request, "core/about.html", context)


def resume(request):
    contact = Contact.objects.first()
    education_items = contact.education.all().order_by("-start_date")
    work_experience_items = contact.experience.all().order_by("-start_date")
    skills = contact.skills.all()
    print(skills)
    skills_by_category = {}
    for skill in skills:
        if skill.category.name not in skills_by_category:
            skills_by_category[skill.category.name] = {"is_percentage": skill.category.is_percentage, "skills": []}
        skills_by_category[skill.category.name]['skills'].append(skill)

    context = {
        "education_items": education_items,
        "work_experience_items": work_experience_items,
        "skills_by_category": skills_by_category
    }

    print(skills_by_category)

    return render(request, "core/resume.html", context)


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
