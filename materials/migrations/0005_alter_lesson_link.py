# Generated by Django 5.0.6 on 2024-06-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="link",
            field=models.URLField(max_length=400, verbose_name="ссылка на видео"),
        ),
    ]
