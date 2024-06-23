from rest_framework import serializers

from users.models import User, Payments, Subscriptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class HistoryPaySerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True)

    class Meta:
        model = User
        fields = ["email", "payments"]


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ["course", ]
