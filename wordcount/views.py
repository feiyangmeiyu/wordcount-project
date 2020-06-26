from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	#return HttpResponse("Hello")
	return render(request, 'home.html')


#def eggs(request):
#	return HttpResponse("Eggs are great!")

def count(request):
	fulltext = request.GET['fulltext']
	#print(fulltext)
	wordlist = fulltext.split()

	worddic = {}

	for word in wordlist:
		if word in worddic:
			#increase
			worddic[word] += 1
		else:
			#add to the dic
			worddic[word] = 1

	sortedwords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), "worddic": sortedwords})

def about(request):
	return render(request, 'about.html')