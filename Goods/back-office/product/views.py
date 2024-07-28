# list ---
# detail ---
# create ---
# update ---
# delete ---

from Goods import models
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductEnterForm
from Goods.models import ProductEnter, Product


def listProduct(request):
    queryset = models.Product.objects.all()
    context = {}
    context['queryset'] = queryset
    return render(request, 'back-office/product/list.html',context)


def detailProduct(request, generate):
    queryset = models.Product.objects.get(generate_code=generate)
    context = {}
    print(models.ProductImg.objects.filter(product=queryset))
    context['queryset'] = queryset
    context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
        # way 1
        # category_id = request.POST['category_id']
        # category = models.Category.objects.get(id=category_id)
        # product = models.Product.objects.create(
        #     name = request.POST['name'],
        #     quantity = request.POST['quantity'],
        #     price = request.POST['price'],
        #     category = category, 
        #     description = request.POST['description']
        # )
        # way 2
        product = models.Product.objects.create(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
            category_id = request.POST['category_id'], 
            description = request.POST['description']
        )

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
        return redirect('listProduct')
    
    return render(request, 'back-office/product/create.html', context)
        

def updateProduct(request, generate):
    product = models.Product.objects.get(generate_code=generate)
    context = {
        'categorys': models.Category.objects.all(),
        'product': product
    }

    if request.method == 'POST':
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.category_id = request.POST['category_id']
        product.save()

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )

        return redirect('listProduct')

    return render(request, 'back-office/product/update.html', context)


def product_enter_list(request):
    product_enters = ProductEnter.objects.all()
    return render(request, 'back-office/product/product_enter_list.html', {'product_enters': product_enters})


def create_product_enter(request):
    context = {'products': Product.objects.all()}

    if request.method == 'POST':
        try:
            product = Product.objects.get(generate_code=request.POST['product_id'])
        except Product.DoesNotExist:
            return render(request, 'back-office/product/create_product_enter.html', {
                'products': Product.objects.all(),
                'error': 'Product not found'
            })

        product_enter = ProductEnter(
            product=product,
            quantity=int(request.POST['quantity']),
            date=request.POST['date'],
            description=request.POST['description']
        )
        product_enter.save()
        return redirect('product_enter_list')

    return render(request, 'back-office/product/create_product_enter.html', context)




def update_product_enter(request, generate):
    product_enter = get_object_or_404(ProductEnter, generate_code=generate)

    if request.method == 'POST':
        form = ProductEnterForm(request.POST, instance=product_enter)
        if form.is_valid():
            product_enter = form.save(commit=False)
            product_enter.save()
            return redirect('product_enter_list')
    else:
        form = ProductEnterForm(instance=product_enter)

    return render(request, 'back-office/product/update_product_enter.html', {'form': form, 'product_enter': product_enter})


def product_enter_detail(request, generate):
    product_enter = get_object_or_404(ProductEnter, generate_code=generate)
    return render(request, 'back-office/product/product_enter_detail.html', {'product_enter': product_enter})


def deleteProduct(request, generate):
    models.Product.objects.get(generate_code=generate).delete()
    return redirect('listProduct')



