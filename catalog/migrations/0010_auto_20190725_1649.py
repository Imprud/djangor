# Generated by Django 2.2.1 on 2019-07-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20190725_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='drive_imgage',
        ),
        migrations.AddField(
            model_name='agency',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logos'),
        ),
    ]
