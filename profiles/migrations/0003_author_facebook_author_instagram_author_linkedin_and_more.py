# Generated by Django 4.1.2 on 2023-09-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_alter_author_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="facebook",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="instagram",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="linkedin",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="twitter",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]