from django.conf.urls import patterns, url

from hrapp import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),

    #### GET (data getters)
    url(r'^recommend/', views.recommend, name="recommend")
)
