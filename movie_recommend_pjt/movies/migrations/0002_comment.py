# Generated by Django 4.2.16 on 2024-11-22 00:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('movies', models.ManyToManyField(related_name='comments', to='movies.movie')),
                ('users', models.ManyToManyField(related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
