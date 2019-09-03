from django.db import models

class Music(models.Model):

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    album = models.ForeignKey('Album', related_name='musics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Album(models.Model):

    title = models.CharField(max_length=200)
    band = models.ForeignKey('Band', related_name='albuns', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.title

class Band(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Member(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey('Band', related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
