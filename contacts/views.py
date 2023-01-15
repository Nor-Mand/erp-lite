from django.shortcuts import render, redirect
from .models import Industries, Countries, Cities
from .forms import FormIndustry, FormCountry, FormCities
from django.core.paginator import Paginator


# Countries
def home_countries(request):
    form = FormCountry()
    if request.method == 'POST':
        form = FormCountry(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contacts:country')
    countries_list = Countries.objects.all()
    paginator = Paginator(Countries.objects.all(), 6)
    page_number = request.GET.get('page')
    page_country = paginator.get_page(page_number)
    context = {
        'form': form,
        'countries_list': countries_list,
        'page_country': page_country,
    }
    return render(request, 'countries.html', context)


def update_country(request, pk):
    country = Countries.objects.get(id=pk)
    if request.method == 'POST':
        form = FormCountry(request.POST, instance=country)
        if form.is_valid():
            form.save()
        return redirect('contacts:country')
    else:
        form = FormCountry(instance=country)
    page_country = Countries.objects.all()
    page_name = request.path
    context = {
        'form': form,
        'page_country': page_country,
        'page_name': page_name,
    }
    return render(request, 'countries.html', context)


def delete_country(request, pk):
    country = Countries.objects.get(id=pk)
    country.delete()
    return redirect('contacts:country')


# Industries
def create_industry(request):
    form = FormIndustry()
    if request.method == 'POST':
        form = FormIndustry(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contacts:industry')
    industries_list = Industries.objects.all()
    paginator = Paginator(Industries.objects.all(), 6)
    page_number = request.GET.get('page')
    page_industry = paginator.get_page(page_number)
    context = {
        'form': form,
        'industries_list': industries_list,
        'page_industry': page_industry,
    }
    return render(request, 'industries.html', context)


def update_industry(request, pk):
    industry = Industries.objects.get(id=pk)
    if request.method == 'POST':
        form = FormIndustry(request.POST, instance=industry)
        if form.is_valid():
            form.save()
        return redirect('contacts:industry')
    else:
        form = FormIndustry(instance=industry)
    page_industry = Industries.objects.all()
    page_name = request.path
    context = {
        'form': form,
        'page_industry': page_industry,
        'page_name': page_name,
    }
    return render(request,'industries.html', context)


def delete_industry(request, pk):
    industry = Industries.objects.get(id=pk)
    industry.delete()
    return redirect('contacts:industry')


# Countries
def home_cities(request):
    form = FormCities()
    if request.method == 'POST':
        form = FormCities(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contacts:cities')
    cities_list = Cities.objects.all()
    paginator = Paginator(Cities.objects.all(), 6)
    page_number = request.GET.get('page')
    page_city = paginator.get_page(page_number)
    context = {
        'form': form,
        'cities_list': cities_list,
        'page_city': page_city,
    }
    return render(request, 'cities.html', context)


def update_cities(request, pk):
    city = Cities.objects.get(id=pk)
    if request.method == 'POST':
        form = FormCities(request.POST, instance=city)
        if form.is_valid():
            form.save()
        return redirect('contacts:cities')
    else:
        form = FormCities(instance=city)
    page_city = Cities.objects.all()
    page_name = request.path
    context = {
        'form': form,
        'page_city': page_city,
        'page_name': page_name,
    }
    return render(request, 'cities.html', context)


def delete_cities(request, pk):
    city = Cities.objects.get(id=pk)
    city.delete()
    return redirect('contacts:cities')