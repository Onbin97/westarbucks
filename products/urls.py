from django.urls import path

from products.views import DrinksView

urlpatterns = [
    path("", DrinksView.as_view())
]