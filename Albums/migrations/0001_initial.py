# Generated by Django 2.2 on 2021-02-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('audio_book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('podcast_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
                ('host', models.CharField(max_length=100)),
                ('participants', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
