from hrapp.recommender.QuerySearch.QuerySearch import RecommenderQS
import time

class RecommendationEngine:
	rqs = None

	def __init__(self):
		start_time = time.time()
		RecommendationEngine.rqs = RecommenderQS(num_hashtags=5000)
		print "Recommendation took: " + str((time.time() - start_time)/60) + " minutes"