from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import shuffle
import sys
from pprint import pprint
from hrapp.recommender.TweetLib import TweetLib


def get_folds(data, num_folds):
	indices = list(xrange(num_folds))*(int((len(data)/num_folds)) + 1)
	indices = indices[:len(data)]
	shuffle(indices)
	folds = []
	for index in xrange(num_folds):
		train_set = []
		test_set = []
		for i,j in enumerate(indices):
			if j == index:
				test_set.append(data[i])
			else:
				train_set.append(data[i])
		folds.append((train_set, test_set))
	return folds


def get_hashtags():
	hashtags = []
	for line in sys.stdin:
		hashtags.append(line.strip())
	return hashtags

class RecommenderQS:
	TWEETS_PER_HASHTAG = 1000
	def __init__(self, hashtags=None, num_hashtags=40, corpus=None):
		self.tl = TweetLib()
		print >> sys.stderr, "Initialising RecommenderQS!"
		if hashtags == None:
			print "Getting top hashtags..."
			top_hashtags = self.tl.get_top_hashtags(num_hashtags)
			self.hashtags = top_hashtags
		else:
			self.hashtags = hashtags

		#print "Creating the corpus..."
		if corpus == None:
			corpus = []
			for hashtag in self.hashtags:
				tweets = self.tl.get_tweets(hashtag, RecommenderQS.TWEETS_PER_HASHTAG)
				tweet_doc = " ".join(tweets)	
				corpus.append(tweet_doc)
		self.vectorizer = TfidfVectorizer()
		self.vectorizer.fit(corpus)
		self.hashtag_vectors = self.vectorizer.transform(corpus)

	def recommend(self, tweet):
		tweet_vec = self.vectorizer.transform([tweet])
		scores = cosine_similarity(tweet_vec[0:1], self.hashtag_vectors)[0]
		return list(reversed([self.hashtags[i[0]] for i in sorted(enumerate(scores), key=lambda x:x[1])]))

if __name__ == "__main__":
	# rqs = RecommenderQS(hashtags=["happy", "sad", "surprised", "relieved"])
	# rqs.recommend("cry crying")
	
	top_hashtags = get_hashtags()
	# rqs = RecommenderQS(hashtags=["happy", "sad", "surprised", "relieved"])
	# print rqs.recommend("cry crying")

	tl = TweetLib()
	for i in xrange(len(top_hashtags) - 2):
		hashtags = top_hashtags[:i+2]
		data = []
		for hashtag in hashtags:
			tweets = tl.get_tweets(hashtag, 1000)
			data = data + [(hashtag, t) for t in tweets]

		folds = get_folds(data, 4)
		

		avg_error = float(0)
		for f in folds:
			train = f[0]
			test = f[1]
			corpus = [""]*(i+2)
			for w in train:
				corpus[hashtags.index(w[0])] = corpus[hashtags.index(w[0])] + " " + w[1]
			rqs = RecommenderQS(hashtags=hashtags,corpus=corpus)
			errors = float(0)
			tot = float(0)
			for w in test:
				predicted = rqs.recommend(w[1])
				if predicted[0] != w[0]:
					errors = errors + 1
				tot = tot + 1
			error_rate = errors/tot
			avg_error = avg_error + error_rate
		avg_error = avg_error/(len(folds))
		
		print str(i+2) + ", " + str(avg_error)
		


