# Generated by Django 4.1.7 on 2023-02-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_detection_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='items',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='detection',
            name='pred',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]