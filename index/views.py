from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()

    cart = Cart(request)
    for product in products:
        product.selected_quantity = cart.cart.get(str(product.id), {}).get('quantity', 0)

    context = {'category': category, 'categories': categories, 'products': products, 'cart_product_form': cart_product_form} # are all these 4 are really used
    return render(request, 'my_product_list.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,'product_detail.html', context={'product': product})