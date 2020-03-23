from django.contrib.auth.models import User
from django.db import models


class Lobby(models.Model):
    hash = models.CharField(max_length=100, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.hash = str(uuid.uuid4())
        super().save(*args, **kwargs)


class Board(models.Model):
    name = models.CharField(max_length=100)


class Tile(models.Model):
    next = models.ForeignKey("self", on_delete=models.DO_NOTHING)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)

    image = models.ImageField()
    message = models.TextField()
    action = models.CharField(max_length=100)


class Player(models.Model):
    lobby = models.ForeignKey("Lobby", on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    drinks = models.IntegerField(default=0)
    tile = models.ForeignKey(Tile, on_delete=models.DO_NOTHING, null=True)
