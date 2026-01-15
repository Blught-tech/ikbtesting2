from pathlib import Path

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # Links each task to a specific user
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='task_uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    @property
    def attachment_is_image(self):
        if not self.attachment:
            return False
        extension = Path(self.attachment.name).suffix.lower()
        return extension in {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

    @property
    def attachment_is_pdf(self):
        if not self.attachment:
            return False
        return Path(self.attachment.name).suffix.lower() == '.pdf'
