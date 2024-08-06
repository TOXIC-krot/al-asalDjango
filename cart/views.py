from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from index.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)

        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']  # Update part is not needed
        )

        response_data = {
            'success': True,
            'quantity': cd['quantity']
        }
        return JsonResponse(response_data)

    # If form is not valid, return an error response
    return JsonResponse({'success': False, 'error': 'Invalid form data'})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'order.html', {'cart': cart})


def order(request):
    cart = Cart(request)
    return render(request, 'order.html', {'cart': cart})