# Generated by Django 4.1 on 2023-02-04 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_skill_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='speciality',
        ),
    ]
