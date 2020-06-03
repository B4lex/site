from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Car

from django.core.paginator import Paginator


class CarsList(View):

    def get(self, request):
        data = Car.objects.all()
        paginator = Paginator(data, 2)
        page = request.GET.get('page')
        data = paginator.get_page(page)
        return render(request, 'cars_list/cars_content.html', {'cars': data})


class CarDetail(View):

    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return render(request, 'cars_list/car_detail.html', {'car': car})
