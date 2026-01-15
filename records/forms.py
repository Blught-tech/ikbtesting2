from pathlib import Path

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'attachment', 'is_completed']
        widgets = {
            'is_completed': forms.CheckboxInput(attrs={'class': 'status-checkbox'}),
            'attachment': forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf'}),
         }    

    def clean_attachment(self):
        attachment = self.cleaned_data.get('attachment')
        if not attachment:
            return attachment

        allowed_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.pdf'}
        allowed_mime_types = {
            'image/png',
            'image/jpeg',
            'image/gif',
            'image/webp',
            'application/pdf',
        }
        extension = Path(attachment.name).suffix.lower()
        content_type = getattr(attachment, 'content_type', '').lower()
        if extension not in allowed_extensions:
            raise forms.ValidationError("Only image or PDF files are allowed.")
        if content_type not in allowed_mime_types:
            raise forms.ValidationError("Only image or PDF files are allowed.")
        max_size = 5 * 1024 * 1024
        if attachment.size > max_size:
            raise forms.ValidationError("Attachment size must be 5MB or less.")
        return attachment

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or len(title.strip()) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) > 500:
            raise forms.ValidationError("Description cannot exceed 500 characters.")
        return description
