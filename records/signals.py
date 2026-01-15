from django.contrib.auth.signals import user_login_failed, user_logged_in
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    username = credentials.get('username', 'Unknown')
    
    # We use the first Superuser as the 'actor' for this system log
    admin_user = User.objects.filter(is_superuser=True).first()
    
    if admin_user:
        LogEntry.objects.create(
            user=admin_user,
            content_type=ContentType.objects.get_for_model(User),
            object_id='0', # Must be a string
            object_repr=f"SECURITY ALERT: Failed Login",
            action_flag=ADDITION,
            change_message=f"Failed login attempt for username: {username}"
        )


@receiver(user_logged_in)
def reset_mfa_verification(sender, request, user, **kwargs):
    request.session['mfa_verified'] = False
