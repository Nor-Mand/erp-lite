from django.shortcuts import render, redirect
from .models import Industries
from .forms import FormIndustry
from django.core.paginator import Paginator


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