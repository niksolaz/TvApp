from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

class TvShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=254)

class Season(models.Model):
    season_number = models.IntegerField(default=1)
    summary = models.CharField(max_length=254)
    tv_show = models.ForeignKey(TvShow)

class Episode(models.Model):
    episode_number= models.IntegerField(default=1)
    summary = models.CharField(max_length=254)
    season = models.ForeignKey(Season)
