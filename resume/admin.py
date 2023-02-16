from django.contrib import admin
from .models import Certificate, Interest, Job, Skill, SkillCategory, Task, University


admin.site.register(Interest)


class JobAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position_name', 'start_date', 'end_date']


admin.site.register(Job, JobAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']


admin.site.register(Skill, SkillAdmin)


class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']


admin.site.register(SkillCategory, SkillCategoryAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'related_job']


admin.site.register(Task, TaskAdmin)

admin.site.register(University)
admin.site.register(Certificate)
