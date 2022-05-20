# Generated by Django 4.0.1 on 2022-02-01 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarsPostComment',
            fields=[
                ('source_id', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
