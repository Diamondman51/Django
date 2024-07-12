from django.urls import path

from .views import all_news

urlpatterns = [
    path('news/', all_news)
]