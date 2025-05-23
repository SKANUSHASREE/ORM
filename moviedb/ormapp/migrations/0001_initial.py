# Generated by Django 5.2.1 on 2025-05-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=100)),
                ('date_of_release', models.DateField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
