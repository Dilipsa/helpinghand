# Generated by Django 3.1.7 on 2021-07-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_taker'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='pin_code',
            field=models.PositiveIntegerField(default=560058),
            preserve_default=False,
        ),
    ]
