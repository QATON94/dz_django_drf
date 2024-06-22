from celery import shared_task
from django.core.mail import send_mail

from dz_django_drf.settings import EMAIL_HOST_USER
from logger import setup_logger
from materials.models import Course
from users.models import Subscriptions

logger = setup_logger()


@shared_task
def check_subs(course_pk):
    logger.info(f'----------------START SUBSCRIPTIONS---------------')
    course = Course.objects.get(id=course_pk)
    subscription = Subscriptions.objects.all().filter(course=course.id, )
    topic = f'Ваш курс {course} обновлен'
    text = f'Ваш курс {course} обновлен'
    recipient_list = []
    if subscription.exists():
        for sub in subscription:
            recipient_list.append(sub.user.email)
        logger.info('--------Отправка сообщения------------------')
        send_mail(
            subject=topic,
            message=text,
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        logger.info('--------Сообщения отправлены------------------')
    else:
        logger.info('--------Нет пользователей подписанных на курс------------------')
    logger.info('--------END SUB------------------')
    return None
