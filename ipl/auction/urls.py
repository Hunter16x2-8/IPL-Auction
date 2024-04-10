from django.urls import path, include
from . import views


urlpatterns = [
    path("bidding/", views.Biding.as_view())
]
