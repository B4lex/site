from django.shortcuts import render
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
