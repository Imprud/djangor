# Generated by Django 2.2.1 on 2019-07-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190710_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
