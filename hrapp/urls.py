from django.conf.urls import patterns, url
from hrapp.RecommendationEngine import RecommendationEngine
from hrapp import views

## initialize the recommendation engine
RecommendationEngine()

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),

    #### GET (data getters)
    url(r'^recommend/', views.recommend, name="recommend")
)
