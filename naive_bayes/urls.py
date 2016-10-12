from django.conf.urls import url

from . import views

app_name = 'naive_bayes'
urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^result/$', views.result, name='result'),
]
