# Generated by Django 4.1.2 on 2023-09-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="about",
            field=models.TextField(default="Hola"),
        ),
    ]
