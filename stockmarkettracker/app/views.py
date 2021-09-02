from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

from app.models import stocks

def index(request):
    context = {}
    
    stock       = []
    start_date  = []
    end_date    = []

    start_dates = list(stocks.objects.values("ticker").annotate(n=models.Min("date")))
    end_dates   = list(stocks.objects.values("ticker").annotate(n=models.Max("date")))

    for i in range(len(start_dates)):
        s, sdate   = start_dates[i].values()
        _, edate   = end_dates[i].values()
        stock.append(s)
        start_date.append(str(sdate.date()))
        end_date.append(str(edate.date()))

    context["stock"]=stock
    context["begin_date"]=start_date
    context["end_date"]=end_date

    return render(request, 'index.html', context)