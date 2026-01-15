from pathlib import Path
import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def task_attachment_upload_path(instance, filename):
    extension = Path(filename).suffix.lower()
    return f"task_uploads/{uuid.uuid4()}{extension}"


class Task(models.Model):
    # Links each task to a specific user
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to=task_attachment_upload_path, blank=True, null=True)

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


class UserMFA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mfa_profile')
    secret = models.CharField(max_length=32)
    is_enabled = models.BooleanField(default=False)
    enabled_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        status = "enabled" if self.is_enabled else "disabled"
        return f"MFA for {self.user.username} ({status})"
