# Generated by Django 4.1.4 on 2023-02-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_application_date_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='skills',
            field=models.CharField(default=None, max_length=700, null=True),
        ),
    ]
