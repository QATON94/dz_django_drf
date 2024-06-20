from django.db import models

from dz_django_drf.settings import AUTH_USER_MODEL


class Course(models.Model):
    """Описание модели Курс"""

    name = models.CharField(max_length=100, verbose_name="название")
    picture = models.ImageField(
        upload_to="course", verbose_name="превью", null=True, blank=True
    )
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="пользователь")

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
    link = models.URLField(max_length=400, verbose_name="ссылка на видео")
    course = models.ForeignKey(Course, related_name='lessons', verbose_name="курс", on_delete=models.CASCADE, null=True,
                               blank=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="пользователь")

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name
