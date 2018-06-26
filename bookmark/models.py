from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    # TODO: Add user author
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # TODO: Tagging, Categories, Description
