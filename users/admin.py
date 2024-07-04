from django.contrib import admin

from users.models import User, Payments


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_activity')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_paid', 'amount_paid')
