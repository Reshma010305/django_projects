from django.shortcuts import render
from .models import Product
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Ultrabook Pro', description='Lightweight laptop with high performance', price='2200')
        Product.objects.create(name='Foldable Phone', description='Innovative foldable screen smartphone', price='1400')
        Product.objects.create(name='Bluetooth Earbuds', description='High-quality sound with long battery life', price='180')
        Product.objects.create(name='Fitness Tracker', description='Monitor health metrics and activities', price='150')
        Product.objects.create(name='E-Reader', description='Perfect device for reading on the go', price='300')
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})