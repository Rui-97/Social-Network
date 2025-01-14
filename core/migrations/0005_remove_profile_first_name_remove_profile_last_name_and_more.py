# Generated by Django 4.2.4 on 2023-09-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_profile_delete_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_imgs/default_profile_img.jpg",
                upload_to="profile_imgs",
            ),
        ),
    ]
