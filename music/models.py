from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    part_text = models.TextField(null=True)

    def __str__(self):
        return str(self.artist) + ' - ' + str(self.title)




