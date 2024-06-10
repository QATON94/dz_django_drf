from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsListAPIView, PaymentsCreateAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register("", UserViewSet, basename="user")

urlpatterns = [
                  path("payments/", PaymentsListAPIView.as_view(), name="payments"),
                  path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
                  path("payments/<int:pk>/", PaymentsRetrieveAPIView.as_view(), name="payments_get"),
                  path("payments/update/<int:pk>/", PaymentsUpdateAPIView.as_view(), name="payments_update"),
                  path("payments/delete/<int:pk>/", PaymentsDestroyAPIView.as_view(), name="payments_delete"),
              ] + router.urls
