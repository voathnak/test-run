from django.conf.urls import patterns, url

from comment import views

urlpatterns = patterns('',
    # ex: /comment/
    url(r'^$', views.index, name='index'),
    # ex: /comment/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /comment/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /comment/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
