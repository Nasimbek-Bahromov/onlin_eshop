from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    infos = models.Info.objects.last()
    context = {
        'banners': banners,
        'info': infos
    }

    return render(request, 'index.html', context)


def admin(request):
    return render(request, 'admin')




