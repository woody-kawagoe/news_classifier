from subprocess import Popen, PIPE
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import pandas as pd


def form(request):
    return render(request, 'naive_bayes/form.html')


def result(request):
    url = request.POST['url']
    p = Popen(["python", "trainer/getBoW.py", url], stdout=PIPE)
    c = p.stdout.readlines()
    if c:
        bow = c[0].decode('utf-8').split(" ")
    else:
        bow = []
    classifier = pd.read_csv("trainer/classifier.csv", index_col=0)
    categories = classifier.columns
    P = {}
    for name in categories:
        P[name] = 0.
    for word in bow:
        for name in categories:
            if word in classifier.index:
                P[name] += classifier.ix[word, name]
    P = sorted(P.items(), key=lambda x: x[1], reverse=True)
    if P[0][1] is 0.0:
        category = "Error"
    else:
        category = P[0][0]
    context = {
        'P': P,
        'category': category,
        'url': url
        }
    return render(request, 'naive_bayes/result.html', context)
