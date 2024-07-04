# Generated by Django 5.0.6 on 2024-06-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_payments_last_login"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="last_login",
        ),
        migrations.AddField(
            model_name="user",
            name="last_activity",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата последней активности"
            ),
        ),
    ]