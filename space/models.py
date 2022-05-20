from django.db import models
import uuid

class PostComment(models.Model):
    source_id = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=200, null = True, blank = True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.source_id)