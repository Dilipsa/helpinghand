# Generated by Django 3.1.7 on 2021-05-02 14:29

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210502_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taker',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
