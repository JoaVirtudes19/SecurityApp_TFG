# Generated by Django 4.1.7 on 2023-02-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_detection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='img',
            field=models.ImageField(upload_to='detections'),
        ),
    ]
