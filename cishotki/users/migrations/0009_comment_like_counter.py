# Generated by Django 2.2.6 on 2019-11-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191110_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]