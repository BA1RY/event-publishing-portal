# Generated by Django 3.0.5 on 2020-04-07 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='profile_pics')),
                ('description', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('attendees', models.ManyToManyField(related_name='attendees', to=settings.AUTH_USER_MODEL)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
