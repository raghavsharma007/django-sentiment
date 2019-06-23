from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob

# Create your views here.

def homepage(request):
    return render(request, 'sent/home.html')

def result(request):
    text = request.POST.get('text','default')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity


    return render(request, 'sent/result.html', {'polarity':polarity})

