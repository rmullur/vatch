# Generated by Django 2.2.7 on 2020-03-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smain_2', '0007_auto_20200303_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='live',
            field=models.BooleanField(default=False),
        ),
    ]
