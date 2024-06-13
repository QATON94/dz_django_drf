import json

from django.core.management import BaseCommand

from dz_django_drf.settings import BASE_DIR
from materials.models import Lesson, Course
from users.models import Payments, User


class Command(BaseCommand):
    @staticmethod
    def json_read_payments():
        payments = []
        payments_path = BASE_DIR.joinpath('data', 'data_payments.json')
        with open(payments_path, "r") as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'users.payments':
                payments.append(item)

        return payments

    def handle(self, *args, **options):
        Payments.objects.all().delete()
        payments_crate = []
        for payment in Command.json_read_payments():
            paid_lesson = Lesson.objects.filter(pk=payment['fields']['paid_lesson']).first()
            paid_course = Course.objects.filter(pk=payment['fields']['paid_course']).first()
            payments_crate.append(
                Payments(id=payment['pk'],
                         user=User.objects.get(pk=payment['fields']['user']),
                         date_paid=payment['fields']['date_paid'],
                         paid_course=paid_course,
                         paid_lesson=paid_lesson,
                         amount_paid=payment['fields']['amount_paid'],
                         payment_method=payment['fields']['payment_method'])
            )

        Payments.objects.bulk_create(payments_crate)
