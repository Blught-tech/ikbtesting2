from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('records', '0003_task_attachment_uuid_uploads'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMFA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=32)),
                ('is_enabled', models.BooleanField(default=False)),
                ('enabled_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mfa_profile', to='auth.user')),
            ],
        ),
    ]
