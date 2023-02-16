from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.db.models import Count
from .models import Certificate, Interest, Job, Skill, SkillCategory, Task, University


def resume(request):
    jobs = Job.objects.order_by('-start_date')
    tasks = Task.objects.values(
        'related_job', 'name'). order_by('related_job', 'name')
    universities = University.objects.order_by('-start_date')
    skills = Skill.objects.values(
        'category', 'name', 'details'). order_by('order')
    skill_categories = SkillCategory.objects.order_by('order')
    certificates = Certificate.objects.order_by('-achievement_date')
    interests = Interest.objects.all()
    return render(request, 'resume/resume.html',
                  {'jobs': jobs, 'tasks': tasks, 'universities': universities,
                   'skills': skills, 'skill_categories': skill_categories,
                   'certificates': certificates, 'interests': interests})
