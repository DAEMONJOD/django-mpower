# Generated by Django 4.1.4 on 2023-02-08 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_application_eid'),
    ]

    operations = [
        migrations.AddField(
            model_name='threads',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
