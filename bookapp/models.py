from django.db import models
import uuid
# Create your models here.

""" 
makemigrations command is used to identify the changes in models.py it also create a migration file.if migration done first time it gives initial = True and have curresponding operations and  do not have dependencies, otherwise it have dependency with older migrations and have the modifations in operation
"""
class BookModal(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)

