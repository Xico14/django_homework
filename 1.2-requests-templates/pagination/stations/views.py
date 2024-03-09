from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        stations_reader = csv.DictReader(csvfile)
        number = int(request.GET.get('page', 1))
        paginator = Paginator(list(stations_reader), 10)
        stations_list = paginator.get_page(number)
    context = {
        'bus_stations': stations_list,
        'page': stations_list,
    }
    return render(request, 'stations/index.html', context)
