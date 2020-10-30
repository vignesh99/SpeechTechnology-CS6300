									#Import libraries
from pylab import *
#!pip install pickle-mixin			#To install pickle
from pickle import dump
from pickle import load
									#Put them in the same folder in which code is running
#words = load(open('words.pkl', 'rb'))
#inds = load(open('inds.pkl', 'rb'))
reps = load(open('reps.pkl', 'rb'))
wordset = load(open('wordset.pkl', 'rb'))

Nreps = 154							#Number of repititions of each word

inds = np.where(reps >= Nreps)[0]
words = wordset[inds]
print(len(inds))
print(words)
									#To use directly in code (for Nreps=154, 36 words)
words = array(['a', 'all', 'an', 'and', 'are', 'ask', 'be', 'carry', 'dark', "don't", 'for', 'greasy', 'had', 'he', 'his', 'in', 'is', 'like', 'me', 'of', 'oily', 'on', 'rag', 'she', 'suit', 'that', 'the', 'to', 'was', 'wash', 'water', 'we', 'with', 'year', 'you', 'your'])