# Generated by Django 2.0.2 on 2018-02-26 23:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todoitem_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
