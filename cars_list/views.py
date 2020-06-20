from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin
from django.db import models
from django.shortcuts import render, redirect

from .forms import UpdateForm
from .models import Car
from .tasks import parsing


class CarsList(ListView):
    model = Car
    template_name = "cars_list/cars_list.html"
    context_object_name = 'cars'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        queryset = Car.objects.all()
        context.update(
            queryset.aggregate(min_price=models.Min('uah_price'),
                               max_price=models.Max('uah_price')),
        )
        return context


class CarDetail(DetailView):
    model = Car
    context_object_name = "car"


class CarsUpdate(FormView):
    form_class = UpdateForm
    template_name = 'cars_list/cars_update.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        params = request.GET
        if params:
            start_page = int(params.get('start_page'))
            task = parsing.delay(start_page)
            return redirect('cars_list')
        else:
            return render(request, self.template_name,
                          {'form': self.form_class()})


