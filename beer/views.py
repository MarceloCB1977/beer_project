from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .forms import *


# Create your views here.
def index(request):
    beer_form = BeerForm()
    return render(request, 'beer/index.html', {'beer_form':beer_form})


def about(request):
    return render(request, 'beer/about.html')


def beer_list(request):
    beer_list = BeerData.objects.all().order_by('style_name')

    p = Paginator(beer_list, 9)
    page = request.GET.get('page')
    beers = p.get_page(page)
    nums = 'a' * beers.paginator.num_pages

    return render(request, 'beer/beer_list.html', {'beer_list':beer_list, 'beers':beers, 'nums':nums})


def style_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        style_search = BeerData.objects.filter(Q(style_name__icontains = searched) | Q(style_key_family__icontains = searched))

        return render(request, 'beer/style_search.html', {'searched':searched, 'style_search':style_search})
    else:
        return render(request, 'beer/style_search.html')


def beer_form(request):
    beer_form = BeerForm()
    return render(request, 'beer/beer_form.html', {'beer_form':beer_form})


def beer_search(request):
    if request.method == 'POST':
        genders = request.POST['gender']
        ages = request.POST['idade']
        abvs = request.POST['abv']
        abv_res = float(abvs.split('-')[0].strip()), float(abvs.split('-')[1].strip())
        srms = request.POST['srm']
        if srms == '0':
            srm_res = (0, 19)
        else:
            srm_res = (20, 200)
        result_search = BeerData.objects.filter(Q(ABV_min__gte = abv_res[0]) & Q(ABV_max__lte = abv_res[1]),
                                                Q(SRM_min__range = srm_res) | Q(SRM_max__range = srm_res))
        return render (request, 'beer/beer_search.html', {'result_search':result_search})
    else:
        return render (request, 'beer/beer_search.html')


def beer_detail(request, beer_id):
    beer = BeerData.objects.get(pk=beer_id)
    return render(request, 'beer/beer_detail.html', {'beer':beer})
