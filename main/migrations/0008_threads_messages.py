# Generated by Django 4.1 on 2023-01-18 12:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_profilevisits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=10485759)),
                ('receiver', models.CharField(max_length=10485759)),
                ('has_unread', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'threads',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_user', models.CharField(max_length=10485759)),
                ('receiver_user', models.CharField(max_length=10485759)),
                ('body', models.CharField(max_length=10000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='messages/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('msg_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.threads')),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
