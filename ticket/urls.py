from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name='homepage'),
    path('ticket/<int:ticket_id>/',generate_ticket, name='ticket'),
]