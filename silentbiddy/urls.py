from django.urls import path
from . import views

urlpatterns = [
    path('submit_bid/', views.submit_bid, name='submit_bid'),  # Bid submission form
]
