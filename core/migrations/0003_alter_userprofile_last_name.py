# Generated by Django 4.2.4 on 2023-08-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_rename_name_userprofile_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
