from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")	

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	wordsandcounts = dict()

	for word in wordlist:
		if word in wordsandcounts:
			wordsandcounts[word] += 1
		else:
			wordsandcounts[word] = 1

	sortedwords = sorted(wordsandcounts.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordlist), 'booger':sortedwords})