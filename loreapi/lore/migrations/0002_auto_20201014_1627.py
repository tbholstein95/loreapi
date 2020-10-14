# Generated by Django 3.1.1 on 2020-10-14 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lore',
            name='adventurerType',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lore',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lore', to=settings.AUTH_USER_MODEL),
        ),
    ]
