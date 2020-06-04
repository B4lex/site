from django.views.generic import ListView, DetailView
from .models import Car


class CarsList(ListView):
    model = Car
    template_name = "cars_list/cars_list.html"
    context_object_name = 'cars'
    paginate_by = 10


class CarDetail(DetailView):
    model = Car
    context_object_name = "car"
