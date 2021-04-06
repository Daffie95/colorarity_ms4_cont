
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

# Importing signals from signals.py
    def ready(self):
        import checkout.signals
