# Generated by Django 4.1.5 on 2023-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_allskills_course_roledetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='careerlevel',
        ),
        migrations.AddField(
            model_name='jobs',
            name='notice_period',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
