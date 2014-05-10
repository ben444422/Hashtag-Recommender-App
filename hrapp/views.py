from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from hrapp.recommender.QuerySearch.test import Test
from hrapp.recommender.QuerySearch.QuerySearch import RecommenderQS
from hrapp.recommender_init import RecommendationEngine



# Create your views here.
def main(request):
	context = {}
	return render(request,'hrapp/main.html')

def recommend(request):
	if request.method == "GET":
		tweet = request.GET.get('tweet', None)
		if tweet == None:
			return HttpResponse(status=400)
		resp = {}
		resp['hashtags'] = RecommendationEngine.rqs.recommend(tweet)
		return HttpResponse(json.dumps(resp), content_type="application/json")
	return HttpResponse(status=501)