from django.db import models
from uuid import uuid4

# Create your models here.


class Note(models.Model):
    # TODO: Add user author
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # TODO: Tagging, Categories


class Bookmark(models.Model):
    # TODO: Add user author
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # TODO: Tagging, Categories, Description
