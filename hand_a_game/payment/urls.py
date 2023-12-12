from django.urls import path
from . import views

urlpatterns = [
  path('payment/<int:notification_id>', views.payment_view, name="payment"),
]