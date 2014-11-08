from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    
    def __unicode__(self):
        return "%s - %s" % (self.username, self.email)
        
    def __str__(self):
        return "%s - %s" % (self.username, self.email)

class TvShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=254)
    
    def __unicode__(self):
        return "%s - %s" % (self.title, self.description)
    
    def __str__(self):
        return "%s - %s" % (self.title, self.description)

class Season(models.Model):
    season_number = models.IntegerField(default=1)
    summary = models.CharField(max_length=254)
    tv_show = models.ForeignKey(TvShow)
    
    def __unicode__(self):
        return "%d - %s" % (self.season_number, self.summary)
    
    def __str__(self):
        return "%d - %s" % (self.season_number, self.summary)

class Episode(models.Model):
    episode_number= models.IntegerField(default=1)
    summary = models.CharField(max_length=254)
    season = models.ForeignKey(Season)
    
    def __unicode__(self):
        return "(TvShow %s - Season %d) Episode: %d" % ( 
            self.season.tv_show.title, 
            self.season.season_number, 
            self.episode_number
        )
