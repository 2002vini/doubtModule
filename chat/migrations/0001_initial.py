# Generated by Django 4.2.1 on 2023-07-08 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.FileField(default='profile_pic/dummy-profile.png', null=True, upload_to='profile_pic')),
                ('last_text', models.CharField(blank=True, max_length=100, null=True)),
                ('online_status', models.BooleanField(default=False)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_educator', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
