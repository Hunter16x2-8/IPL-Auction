from django.db import models

# Create your models here

class Team(models.Model):
    team = models.CharField(max_length = 50)
    # initial_funds = models.IntegerField()
    funds_left = models.FloatField()

    def __str__(self) -> str:
        return self.team

class Player(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.FloatField()
    final_price = models.FloatField(blank=True, null=True)
    points = models.IntegerField()
    sold_to = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name