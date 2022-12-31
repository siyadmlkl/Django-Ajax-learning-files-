from django.shortcuts import render
from .models import Assets
from django.http import JsonResponse


def home(request):
    areas = Assets.objects.values('area').distinct()
    return render(request, 'index.html', {'areas': areas})


def selectLocation(request):
    data = []
    _area = request.GET.get('area')
    assets = Assets.objects.filter(area=_area)

    for asset in assets:
        data.append(asset.location)
    data = tuple(set(data))

    if request.is_ajax():
        return JsonResponse({'data': data})
        
    return render(request, 'index.html')


def selectAssets(request):
    data = []
    _area = request.GET.get('area')
    _location = request.GET.get('location')
    assets = Assets.objects.filter(area=_area, location=_location)

    for asset in assets:
        data.append(asset.asset)
    
    if request.is_ajax():
        return JsonResponse({'data': data})

    return render(request, 'index.html')
