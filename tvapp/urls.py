from django.conf.urls import patterns, include, url
from tvapp import views

urlpatterns = patterns("",
    url(r'^$',views.HomeView, name='HomeView'),
    url(r'^users/(?P<username_id>\w+)/$',views.UserView, name='UserView'),
    url(r'^users/$',views.UsersView, name='UsersView'),
    url(r'^tvshows/$',views.TvShowsView, name='TvShowsView'),
    url(r'^tvshows/last/$',views.LastReleases, name='LastReleases'),
    url(r'^tvshows/(?P<tv_show_title>\w+)/$',views.TvShowView, name='TvShowView'),
    url(r'^tvshows/(?P<tv_show_title>\w+)/seasons/$',views.SeasonsView, name='SeasonsView'),
    url(r'^tvshows/(?P<tv_show_title>\w+)/seasons/(?P<season_number>\d+)/$',views.SeasonView, name='SeasonView'),
    url(r'^tvshows/(?P<tv_show_title>\w+)/seasons/(?P<season_number>\d+)/episodes/$',views.EpisodesView, name='EpisodesView'),
    url(r'^tvshows/(?P<tv_show_title>\w+)/seasons/(?P<season_number>\d+)/episodes/(?P<episode_number>\d+)/$',views.EpisodeView, name='EpisodeView'),
    
)