# Generated by Django 4.0.1 on 2022-02-02 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_rename_marspostcomment_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
