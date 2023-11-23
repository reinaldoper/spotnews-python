from django.urls import path
from news.views import index, new_details


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", new_details, name="news-details-page"),
]