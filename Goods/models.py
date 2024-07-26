from django.db import models
from django.contrib.auth.models import User
from random import sample
import string


class GenerateCode(models.Model):
    generate_code = models.CharField(max_length=255, blank=True, unique=True, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(GenerateCode, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Banner(GenerateCode):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(GenerateCode):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category-images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generate_code = models.CharField(max_length=255, blank=True, unique=True)

    def str(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(GenerateCode, self).save(*args, **kwargs)

class Product(GenerateCode):
    name:str = models.CharField(max_length=255)
    quantity:int = models.PositiveIntegerField(default=1)
    price:float = models.DecimalField(max_digits=8, decimal_places=2)
    category:Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description:str = models.TextField()
    

    def __str__(self):
        return self.name
    
class ProductEnter(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank = True)
    date = models.DateTimeField()
    description = models.TextField()

    def str(self):
        return self.product.name
    
    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.old_quantity = self.product.quantity
            self.product.quantity += self.quantity
        else:
            self.product.quantity -= ProductEnter.objects.get(generate_code=self.generate_code).quantity
            self.product.quantity += self.quantity


class ProductImg(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product-img')

    def __str__(self):
        return self.product.name

class Cart(GenerateCode):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    shopping_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author.username

class CartProduct(GenerateCode):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Order(GenerateCode):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    status = models.SmallIntegerField(
        choices=(
            (1, 'Tayyorlanmoqda'),
            (2, 'Yo`lda'),
            (3, 'Yetib borgan'),
            (4, 'Qabul qilingan'),
            (5, 'Qaytarilgan'),
        )
    )

    def __str__(self):
        return self.full_name
    
class Info(GenerateCode):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    email = models.EmailField()

