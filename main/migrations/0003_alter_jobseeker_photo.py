# Generated by Django 4.1 on 2023-01-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_jobseeker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='main/media/photos/'),
        ),
    ]
