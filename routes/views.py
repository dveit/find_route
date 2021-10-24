from django.shortcuts import render
from django.contrib import messages
from routes.forms import RouteForm
from routes.utils import get_routes

# Create your views here.

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
                return render(request, 'routes/home.html', context)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/home.html', {'form': form})