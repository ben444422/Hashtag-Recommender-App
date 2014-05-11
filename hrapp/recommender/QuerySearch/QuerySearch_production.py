from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from hrapp.recommender.TweetLib import TweetLib


class RecommenderQS:
	def __init__(self, num_hashtags=40):
		self.tl = TweetLib()

		print "Creating the corpus..."
		documents = self.tl.get_hastag_documents(num_hashtags)
		corpus = [b for a,b in documents]
		self.hashtags = [a for a,b in documents]

		self.vectorizer = TfidfVectorizer(stop_words="english")
		self.vectorizer.fit(corpus)
		self.hashtag_vectors = self.vectorizer.transform(corpus)

	def recommend(self, tweet):
		tweet_vec = self.vectorizer.transform([tweet])
		scores = cosine_similarity(tweet_vec[0:1], self.hashtag_vectors)[0]
		return list(reversed([self.hashtags[i[0]] for i in sorted(enumerate(scores), key=lambda x:x[1])]))

if __name__ == "__main__":
	rqs = RecommenderQS(num_hashtags=1000)
	print rqs.recommend("nfl")

		


