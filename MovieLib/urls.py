from django.conf.urls import patterns, url
from MovieLib import views

urlpatterns = patterns('',
	 url(r'^create$', views.CreateView.as_view(), name='movie_create'), #new line
	 url(r'^$', views.IndexView.as_view(), name= 'movie_index'),
	 url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='movie_edit'),
	 url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movie_delete'),
	 url(r'^impressum$', views.ImpressumView.as_view(), name='imp')
)
