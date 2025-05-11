# from django.shortcuts import render
# from django.views import View
# 
# 
# class IndexView(View):
#     def get(self, request):
#         return render(request, "products/index.html")
# 
# 
# index = IndexView.as_view()
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()[:6]  # 人気商品6件
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.exclude(pk=pk)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def cart(request):
    return render(request, 'cart.html')