# Generated by Django 4.2.4 on 2023-08-29 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("bitrh_date", models.DateField(blank=True, null=True)),
                ("bio", models.TextField(blank=True, max_length=500, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="uploads/profile_imgs/default.pgn",
                        upload_to="uploads/profile_imgs",
                    ),
                ),
            ],
        ),
    ]
