# Generated by Django 4.2.4 on 2023-09-04 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="body",
            new_name="caption",
        ),
    ]