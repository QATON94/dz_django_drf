import stripe

from dz_django_drf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_price(amount):
    """Создает цену в страйпе."""

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "price"},
    )


def create_stripe_sessions(price):
    """Создает сессию на оплату в страйпе."""

    print(price)
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
