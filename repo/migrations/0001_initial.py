# Generated by Django 4.1.2 on 2023-09-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0003_author_facebook_author_instagram_author_linkedin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("tags", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="media/docs"),
                ),
                ("participants", models.ManyToManyField(to="profiles.author")),
            ],
        ),
    ]
