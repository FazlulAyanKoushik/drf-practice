from django.db import models
from core.models import BaseModel
from artist.models import Artist

# Create your models here.
class Album(BaseModel):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return f"{self.title}"

