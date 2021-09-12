# Generated by Django 3.2.7 on 2021-09-11 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_auto_20210911_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborator',
            name='user',
        ),
        migrations.AddField(
            model_name='collaborator',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='collaborators', to='auth.user'),
            preserve_default=False,
        ),
    ]