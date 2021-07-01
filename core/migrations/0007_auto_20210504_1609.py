# Generated by Django 3.1.7 on 2021-05-04 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20210504_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('publish', models.BooleanField(default=True)),
                ('feedback_giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_giver', to=settings.AUTH_USER_MODEL)),
                ('feedback_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
