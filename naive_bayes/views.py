from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import trainer.getBow
import pandas as pd


def form(request):
    return render(request, 'naive_bayes/form.html')


def result(request):
    url = request.POST['url']
    bow = trainer.getBoW.getBoW(url)
    classifier = pd.read_csv("trainer/classifier.csv", index_col=0)
    categories = classifier.columns
    P = {category: 0 for for category in categories}
    for word in bow:
        for category in categories:
            if word in classifier.index:
                P[category] += classifier.ix[word, category]
    P = sorted(P.items(), key=lambda x: x[1], reverse=True)
    if P[0][1] is 0.0:
        result_category = "Error"
    else:
        result_category = P[0][0]
    context = {
        'P': P,
        'category': result_category,
        'url': url
        }
    return render(request, 'naive_bayes/result.html', context)
