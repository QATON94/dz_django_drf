from django.db import models


class Course(models.Model):
    """Описание модели Курс"""

    name = models.CharField(max_length=100, verbose_name="название")
    picture = models.ImageField(
        upload_to="course", verbose_name="превью", null=True, blank=True
    )
    description = models.TextField(verbose_name="описание")

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Описание модели Урок"""

    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    picture = models.ImageField(
        upload_to="lesson", verbose_name="превью", null=True, blank=True
    )
    link = models.CharField(max_length=300, verbose_name="ссылка на видео")

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name
