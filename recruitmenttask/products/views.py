from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products/products.html', context)


def product(request, pk):
    productObj = Product.objects.get(id=pk)
    print('productObj', productObj)
    return render(request, 'products/single-product.html', {'product': productObj})


def createProduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  #zapisuje produkt
            return redirect('products')  #wracamy na str główną

    context = {'form': form}
    return render(request, "products/product_form.html", context)


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product) #4.13
        if form.is_valid():
            form.save()  #zapisuje produkt
            return redirect('products')  #wracamy na str główną

    context = {'form': form}
    return render(request, "products/product_form.html", context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'object': product}
    return render(request, 'products/delete_product.html', context)






