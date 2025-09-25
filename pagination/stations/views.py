import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # Открываем файл и читаем его содержимое
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        bus_stations_list = list(reader)

    # Получаем номер текущей страницы из GET-параметра 'page'
    current_page_number = request.GET.get('page', 1)

    # Создаем объект Paginator с 10 записями на страницу
    paginator = Paginator(bus_stations_list, 10)

    # Получаем объект страницы
    page_obj = paginator.get_page(current_page_number)

    # Формируем контекст для шаблона
    context = {
        'bus_stations': page_obj.object_list,
        'page': page_obj,
    }

    return render(request, 'stations/index.html', context)
