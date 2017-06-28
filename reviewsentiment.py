'''
sentiment analysis for movie reviews
'''

import parser
from random import shuffle
from math import floor

def load_data(path):
	dataset = parser.parse(path, "pos", "neg")
	shuffle(dataset)
	shuffle(dataset)
	# return (dev, test)
	return (dataset[:floor(len(dataset)*0.7)], dataset[floor(len(dataset)*0.7) + 1:])
