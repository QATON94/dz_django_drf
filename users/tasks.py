from datetime import timedelta, date

from celery import shared_task

from users.models import User


@shared_task
def user_deactivate():
    users = User.objects.all()
    today = date.today()
    for user in users:
        if today - user.last_activity > timedelta(days=30):
            user.is_active = False
            user.save()
