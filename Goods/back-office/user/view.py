from django.shortcuts import render, redirect

from Goods import models


def myCart(request):
    cart = models.Cart.objects.get(
        author=request.user,
        is_active=True)
    context = {}
    context['cart'] = cart
    return render(request, 'user/cart/detail.html')


def addProductToCart(request, generate_code, quantity):
    product = models.Product.objects.get(generate_code=generate_code)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart, product=product)
        cart_product.quantity += quantity
        cart_product.save()
    except models.CartProduct.DoesNotExist:
        cart_product = models.CartProduct.objects.create(
            product=product,
            cart=cart,
            quantity=quantity
        )
    return redirect('cart_detail')


def substractProductFromCart(request, generate_code, quantity):
    product = models.Product.objects.get(generate_code=generate_code)
    product_cart = models.CartProduct.objects.get(cart__author=request.user, product=product)
    product_cart.quantity -= quantity
    product_cart.save()
    if product_cart.quantity <= 0:
        product_cart.delete()
    return redirect('cart_detail')


def deleteProductCart(request, generate_code):
    product = models.Product.objects.get(generate_code=generate_code)
    product_cart = models.CartProduct.objects.get(cart__author=request.user, product=product)
    product_cart.delete()
    return redirect('cart_detail')


def CreateOrder(request):
    cart = models.Cart.objects.get(
        author=request.user,
        is_active=True
    )

    cart_products = models.CartProduct.objects.filter(cart=cart)

    done_products = []

    for cart_product in cart_products:
        if cart_product.quantity <= cart_product.product.quantity:
            cart_product.product.quantity -= cart_product.quantity
            cart_product.product.save()
            done_products.append(cart_product)
        else:
            for product in done_products:
                product.product.quantity += product.quantity
                product.product.save()
            raise ValueError('Qoldiqda kamchilik')

    models.Order.objects.create(
        cart=cart,
        full_name=f"{request.user.first_name} {request.user.last_name}",
        email=request.user.email,
        phone=request.GET['phone'],
        address=request.GET['address'],
        status=1
    )
    cart.is_active = False
    cart.save()

    return redirect('order_confirmation')


