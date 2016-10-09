from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def form(request):
    return render(request, 'naive_bayes/form.html')

def result(request,category):
    context={'category':category}
    return render(request, 'naive_bayes/result.html', context)

def classifier(request):
    category=request.POST['url']
    return HttpResponseRedirect(reverse('naive_bayes:result', args=(category,)))
