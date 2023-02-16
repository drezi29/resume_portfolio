from django.db import models
from django.utils.translation import gettext_lazy as _


class University(models.Model):
    name_of_school = models.CharField(max_length=128)
    field_of_study = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Universities")

    def __str__(self):
        return (self.name_of_school + ' ' + str(self.start_date))


class Job(models.Model):
    company_name = models.CharField(max_length=32)
    position_name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Task(models.Model):
    name = models.CharField(max_length=255)
    related_job = models.ForeignKey(Job, on_delete=models.CASCADE)


class SkillCategory(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = _("Skill Categories")

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    order = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


class Interest(models.Model):
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='resume/images')

    def __str__(self):
        return self.description


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    achievement_date = models.DateField()

    def __str__(self):
        return self.name
