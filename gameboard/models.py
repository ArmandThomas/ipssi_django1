from django.db import models

# Create your models here.

class GameBoard(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image_url = models.CharField(max_length=250)
    year = models.DateField(default="2021-01-01")
    description = models.CharField(max_length=1000, default="No description available")
    number_of_players = models.IntegerField(default=1)
    duration = models.IntegerField(default=0)
    publisher = models.ForeignKey('GamePublisher', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField('GameBoardCategory')

    def __str__(self):
        return self.name

class GameBoardCategory(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class GamePublisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
