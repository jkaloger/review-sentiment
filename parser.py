'''
Jack Kaloger 2017
parser for review polarity data
from https://www.cs.cornell.edu/people/pabo/movie-review-data/
'''

import os

def parse(path, pos, neg):
    out = []
    poles = [pos, neg]
    for pole in poles:
        for filename in os.listdir(path + pole):
            f = open(path + pole + '/' + filename, 'r')
            out.append({"sentiment": pole, "text": f.read()})

    return out
