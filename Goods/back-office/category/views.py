# list +-+-
# detail +-+-
# create +-+-
# update +-+-
# delete +-+-

from django.shortcuts import render, redirect

from Goods import models


def listCategory(request):
    queryset = models.Category.objects.all()
    
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/category/list.html', context)


def detailCategory(request, generate):
    queryset = models.Category.objects.get(generate_code=generate)
    
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/category/detail.html', context)


def createCategory(request):
    models.Category.objects.create(
        name=request.POST['name']
    )
    return redirect('listCategory')


def updateCategory(request):
    generate_code = request.POST.get('generate_code')
    queryset = models.Category.objects.get(generate_code=generate_code)
    queryset.name = request.POST['name']
    queryset.save()

    return redirect('listCategory')


def deleteCategory(request, generate):
    models.Category.objects.get(generate_code=generate).delete()
    return redirect('listCategory')