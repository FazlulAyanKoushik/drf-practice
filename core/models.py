import uuid
from django.db import models
from dirtyfields import DirtyFieldsMixin


# Create your models here.
class BaseModel(DirtyFieldsMixin, models.Model):
    uuid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def get_auto_fields(self):
        fields = [
            "updated_at",
        ]
        return fields
