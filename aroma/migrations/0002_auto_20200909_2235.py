# Generated by Django 3.1.1 on 2020-09-09 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='sku',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
