from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, PaymentsCreateAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView, UserCreateAPIView, SubscriptionsAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(), name="payments"),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
    path("payments/<int:pk>/", PaymentsRetrieveAPIView.as_view(), name="payments_get"),
    path("payments/update/<int:pk>/", PaymentsUpdateAPIView.as_view(), name="payments_update"),
    path("payments/delete/<int:pk>/", PaymentsDestroyAPIView.as_view(), name="payments_delete"),

    path("register/", UserCreateAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('subs/', SubscriptionsAPIView.as_view(), name='subs'),
]
