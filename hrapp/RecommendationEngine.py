from hrapp.recommender.NaiveBayes.NaiveBayes_production import RecommenderNB
from hrapp.recommender.QuerySearch.QuerySearch_production import RecommenderQS
import time

class RecommendationEngine:
	rqs = None
	rnb = None
	num_hashtags = 200
	def __init__(self):
		start_time = time.time()
		RecommendationEngine.rnb = RecommenderNB(num_hashtags=RecommendationEngine.num_hashtags)
		print "Recommendation took: " + str((time.time() - start_time)/60) + " minutes"