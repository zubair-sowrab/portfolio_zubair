from django.shortcuts import render
from .models import Experience, Education, Project, Certification, Skill, SiteSetting, ExtraCurricular, Reference

def portfolio_home(request):
    """Renders the main hub/overview page."""
    context = {
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/home.html', context)

def experience_view(request):
    """Renders the dedicated experience page."""
    context = {
        'experiences': Experience.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/experience.html', context)

def education_view(request):
    """Renders the dedicated education page."""
    context = {
        'education': Education.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/education.html', context)

def projects_view(request):
    """Renders the dedicated projects page."""
    context = {
        'projects': Project.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/projects.html', context)

def skills_view(request):
    """Renders the dedicated skills page."""
    context = {
        'hard_skills': Skill.objects.filter(skill_type='HARD'),
        'soft_skills': Skill.objects.filter(skill_type='SOFT'),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/skills.html', context)

def certifications_view(request):
    """Renders the dedicated certifications page."""
    context = {
        'certifications': Certification.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/certifications.html', context)

def extracurriculars_view(request):
    """Renders the dedicated extracurriculars page."""
    context = {
        'extracurriculars': ExtraCurricular.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/extracurriculars.html', context)

def references_view(request):
    """Renders the dedicated references page."""
    context = {
        'references': Reference.objects.all(),
        'settings': SiteSetting.objects.first(),
    }
    return render(request, 'portfolio/references.html', context)