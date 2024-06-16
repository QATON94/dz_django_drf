from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from materials.models import Course
from users.models import User, Payments, Subscriptions
from users.serializers import UserSerializer, PaymentsSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['date_paid']


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()


class SubscriptionsAPIView(generics.ListAPIView):
    """Добавление подписки"""

    queryset = Subscriptions.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data['course']
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscriptions.objects.all().filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            subs_item = Subscriptions.objects.create(user=user, course=course_item)
            subs_item.save()
            message = 'подписка добавлена'
        return Response({'message': message})
