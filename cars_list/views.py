from django.shortcuts import render
from django.views.generic import View
from .models import Car


class CarsList(View):

    def get(self, request):
        data = Car.objects.all()
        return render(request, 'cars_list/cars_content.html', {'cars': data})
