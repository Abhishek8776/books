from django.db import models
import uuid
# Create your models here.


class BookModal(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)

