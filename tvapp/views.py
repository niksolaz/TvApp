from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello World")

def UserView(request,username_id):
    return 'this is the user %s' % (username_id,)

def HomeView(request):
    return HttpResponse("HomeView")

def TvShowView(request,tv_show_title=None):
    if tv_show_title is None:
        return 'this is the list of title series  ' 
    else:
        return 'this is the show %s' % (tv_show_title, )
        
def SeasonView(request,season_number=None):
    if season_number is None:
        list_seasons =  'this is the list of season'
        return list_seasons
    else:
        return 'info about season %s' % (season_number, )

def EpisodeView(request,episode_number=None):
    list_episode = 'this is the list of episode %s'
    return list_episode % (episode_number,)

def LastReleases(request):
    return HttpResponse("Release")