from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    singer_name=models.CharField(max_length=200)
    def __str__(self):
        return self.album_name+" - "+" - "+self.singer_name
	

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    singer_name = models.CharField(max_length=200)
    def __str__(self):
        return self.song_name+" - "+self.singer_name