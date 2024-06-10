from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, unique=True, verbose_name="phone")
    city = models.CharField(max_length=50, unique=True, verbose_name="city")
    avatar = models.ImageField(
        upload_to="avatars", default="avatars/default.png", verbose_name="аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):

    METHOD_PAY = [('card', 'оплата картой'), ('cash', 'наличные')]

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True, blank=True)
    date_paid = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', null=True, blank=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=30, choices=METHOD_PAY, verbose_name='способ оплаты',)
