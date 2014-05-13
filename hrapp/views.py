from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
import urllib 
from hrapp.RecommendationEngine import RecommendationEngine




# Create your views here.
def main(request):
	context = {}
	return render(request,'hrapp/main.html')


def recommend(request):
	if request.method == "GET":
		tweet = urllib.unquote(request.GET.get('tweet', None)).decode('utf8')
		if tweet == None:
			return HttpResponse(status=400)
		resp = {}
		if RecommendationEngine.rnb is None:
			RecommendationEngine.rnb = RecommenderNB(num_hashtags=RecommendationEngine.num_hashtags)
		hashtags = RecommendationEngine.rnb.recommend(tweet)
		if hashtags == None:
			resp['hashtags'] = []
		else:
			print hashtags[:10]
			resp['hashtags'] = hashtags
		return HttpResponse(json.dumps(resp), content_type="application/json")
	return HttpResponse(status=501)