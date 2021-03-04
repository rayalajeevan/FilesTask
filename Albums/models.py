from django.db import models

# Create your models here.

class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    duration=models.IntegerField()#In seconds
    uploaded_on=models.DateTimeField()

    def __str__(self):
        return self.name


class Podcast(models.Model):
    podcast_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    duration=models.IntegerField()#In seconds
    uploaded_on=models.DateTimeField()
    host=models.CharField(max_length=100)
    participants=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class AudioBook(models.Model):
    audio_book_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    narrator=models.CharField(max_length=100)
    duration=models.IntegerField()#In seconds
    uploaded_on=models.DateTimeField()

    def __str__(self):
        return self.title