from django.db import models
from core.models import BaseModel
from artist.models import Artist
from album.models import Album


# Create your models here.
class Song(BaseModel):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.PositiveSmallIntegerField()
    release_date = models.DateField()


    def __str__(self):
        return f"{self.title}"
