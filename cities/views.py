from django.shortcuts import get_object_or_404, render
from cities.models import City

# Create your views here.

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    cities = City.objects.all()
    context = {'objects_list': cities}
    return render(request, 'cities/home.html', context)