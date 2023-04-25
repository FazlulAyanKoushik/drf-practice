
from django.urls import path
from artist import views

urlpatterns = [
    path("", views.ArtistRegistration.as_view(), name="artist-register")
]