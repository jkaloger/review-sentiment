'''
sentiment analysis for movie reviews
'''

import parser
from random import shuffle
from math import floor
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data(path):
	dataset = parser.parse(path, "pos", "neg")
	shuffle(dataset)
	shuffle(dataset)
	# return (dev, test)
	return (dataset[:floor(len(dataset)*0.7)],
		    dataset[floor(len(dataset)*0.7) + 1:])

def acc(predicted, real):
	i=0
	for p,r in zip(predicted, real):
		if(p==r):
			i+=1
	return i/len(predicted)


dataset = load_data("data/")
vectorizer = TfidfVectorizer(analyzer="word", ngram_range=(1,2))
X = vectorizer.fit_transform([x["text"] for x in dataset[0]])
nb = GaussianNB()
nb.fit(X.toarray(), [x["sentiment"] for x in dataset[0]])
labels = nb.predict(vectorizer.transform([x["text"] for x in dataset[1]]).toarray())
print(acc(labels, [x["sentiment"] for x in dataset[1]]))
