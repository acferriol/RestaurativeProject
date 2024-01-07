# Generated by Django 4.1.2 on 2023-09-15 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_author_facebook_author_instagram_author_linkedin_and_more"),
        ("posts", "0002_post_about"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="img",
        ),
        migrations.AlterField(
            model_name="post",
            name="participants",
            field=models.ManyToManyField(related_name="authors", to="profiles.author"),
        ),
        migrations.CreateModel(
            name="ImagePost",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="media/posts"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="posts.post",
                    ),
                ),
            ],
        ),
    ]