from django.db.models import query
from django.shortcuts import get_object_or_404, render
from cities.forms import CityForm
from cities.models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

__all__ = (
    'home', 'CityDetailView', 'CityCreateView','CityUpdateView', 'CityDeleteView',
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     city = get_object_or_404(City, id=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    cities = City.objects.all()
    context = {'objects_list': cities, 'form': form}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)