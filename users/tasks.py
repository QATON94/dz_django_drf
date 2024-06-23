from datetime import timedelta, date

from celery import shared_task

from logger import setup_logger
from users.models import User

logger = setup_logger()


@shared_task
def user_deactivate():
    logger.info(f'----------------START user_deactivate---------------')
    users = User.objects.all()
    today = date.today()
    logger.info(f'----------------{users}---------------')
    for user in users:
        logger.info(f'----------------{user}---------------')
        print(user.last_activity - today)
        if today - user.last_activity > timedelta(days=30):
            logger.info(f'--------------{user.is_active}-----------------')
            user.is_active = False
            logger.info(f'--------------{user.is_active}-----------------')
            user.save()
            logger.info(f'--------------user_deactivate-----------------')

    logger.info(f'----------------END---------------')
