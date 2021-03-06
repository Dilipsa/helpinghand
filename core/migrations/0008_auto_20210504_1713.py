# Generated by Django 3.1.7 on 2021-05-04 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20210504_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_thing', models.TextField()),
                ('approve', models.BooleanField(default=False)),
                ('volunteer_giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_giver', to=settings.AUTH_USER_MODEL)),
                ('volunteer_taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_taker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.DeleteModel(
            name='Scheme',
        ),
        migrations.RemoveField(
            model_name='voluntere',
            name='user',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Voluntere',
        ),
    ]
