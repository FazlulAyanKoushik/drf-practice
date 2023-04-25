from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Artist(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.user.first_name and self.user.last_name:
            self.name = f"{self.user.first_name} {self.user.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"