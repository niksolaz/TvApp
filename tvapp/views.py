from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def HomeView(request):
    return HttpResponse("HomeView")

def UsersView(request):
    return HttpResponse('this is list of users')

def UserView(request,username_id):
    return HttpResponse('this is the user %s' % (username_id,))

def TvShowsView(request):
    return HttpResponse('this is the list of tv show')

def TvShowView(request,tv_show_title=None):
    return HttpResponse('This is the tv show %s' % (tv_show_title,) )
    
def SeasonsView(request,tv_show_title=None):
    return HttpResponse('This is the list of seasons for the tv show %s' % (tv_show_title,))
      
def SeasonView(request,tv_show_title=None, season_number=None):
    return HttpResponse('info about season %s of %s' % (season_number, tv_show_title,))

def EpisodesView(request,tv_show_title=None, season_number=None):
    list_episode = 'this is the list of episodes for the show %s in season %s'
    return HttpResponse(list_episode % (tv_show_title,season_number,))

def EpisodeView(request,tv_show_title=None, season_number=None, episode_number=None):
    list_episode = 'this is the episode #%s (TVShow: %s - Season: %s)'
    return HttpResponse(list_episode % (episode_number, tv_show_title, season_number, ))

def LastReleases(request):
    return HttpResponse("The last releases from all the shows")