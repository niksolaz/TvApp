from django.conf.urls import patterns, include, url
from tvapp import views

urlpatterns = patterns("",url(r'^$',views.index, name='index'),
                        url(r'^(?P<username_id>)/$',views.UserView, name='UserView'),
                        url(r'^$',views.HomeView, name='HomeView'),
                        url(r'^(?P<tv_show_title>)/$',views.TvShowView, name='TvShowView'),
                        url(r'^(?P<season_number>)/$',views.SeasonView, name='SeasonView'),
                        url(r'^(?P<episode_number>)/$',views.EpisodeView, name='EpisodeView'),
                        url(r'^$',views.LastReleases, name='LastReleases'),
)