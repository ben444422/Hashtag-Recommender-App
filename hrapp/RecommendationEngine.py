from hrapp.recommender.QuerySearch.QuerySearch_production import RecommenderQS
import time

class RecommendationEngine:
	rqs = None

	def __init__(self):
		start_time = time.time()
		RecommendationEngine.rqs = RecommenderQS(num_hashtags=7000)
		print "Recommendation took: " + str((time.time() - start_time)/60) + " minutes"