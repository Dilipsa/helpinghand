# Generated by Django 3.1.7 on 2021-07-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210716_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taker',
            name='volunteer_status',
            field=models.BooleanField(default=False),
        ),
    ]