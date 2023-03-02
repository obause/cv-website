from django.shortcuts import render
from django.template import RequestContext
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from .models import Contact, Interests, WorkExperience
from .forms import ContactForm
from github.models import GitHubUser

from app.tasks import demo_task

CONTACT_PK = settings.CONTACT_PK


def test(request):
    demo_task("Hello world!", repeat=1, repeat_until=None)
    print("test")
    return render(request, "core/test.html")


def home(request):
    # contact = Contact.objects.first()

    return render(request, "core/main.html")


def about(request):
    contact = Contact.objects.get(pk=CONTACT_PK)
    all_interests = contact.interests.all()
    # context = {"interest_rows": []}
    # row = 0
    # row_content = []
    # for i, interest in enumerate(all_interests):
    #     print(i, interest)
    #     row_content.append(interest)
    #     if i % 2 == 1:
    #         context['interest_rows'].append(row_content)
    #         row_content = []
    # if len(row_content) > 0:
    #     context['interest_rows'].append(row_content)

    fun_facts = contact.fun_facts.all()

    github_user = contact.github_user.get()
    stats = github_user.stats

    sorted_languages = stats.language.all().order_by("-size")[:6]
    # sorted_languages = sorted(languages.items(), key=lambda x: x[1].size, reverse=True)
    # print(sorted_languages)

    context = {
        "interests": all_interests,
        "fun_facts": fun_facts,
        "stats": {
            "name": stats.name,
            "stars": stats.stars,
            "contributions": stats.contributions,
            "repos": stats.repositories,
            "forks": stats.forks,
            "lines_changed": stats.get_loc_changed(),
            "views": stats.page_views,
            "last_updated": stats.last_updated,
        },
        "languages": sorted_languages
    }

    return render(request, "core/about.html", context)


def resume(request):
    contact = Contact.objects.get(pk=CONTACT_PK)
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


class ContactView(View):
    def get(self, request, success=None):
        context = {
            "form": ContactForm(),
            "success": success
        }
        return render(request, "core/contact.html", context)

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            comment = contact_form.save(commit=False)
            comment.save()
            success = True
            return HttpResponseRedirect(reverse("contact", args=[success]))

        context = {
            "form": contact_form
        }
        return render(request, "core/contact.html", context)
