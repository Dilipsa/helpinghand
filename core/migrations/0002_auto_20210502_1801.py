# Generated by Django 3.1.7 on 2021-05-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taker',
            name='email',
            field=models.EmailField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taker',
            name='first_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taker',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]