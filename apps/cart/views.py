import json
from django.http import JsonResponse
from django.views import View, generic
from django.shortcuts import render
from apps.products.models import Product
from apps.cart.cart import Cart


class CartUpdateView(View): # Shouldn't they be generic.TemplateView
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        product_id = data.get("product_id")
        action = data.get("action")

        cart = Cart(request)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product does not exist."}, status=404)

        if action == "increment":
            cart.add(product, quantity=1)
        elif action == "decrement":
            cart.add(product, quantity=-1)
        elif action == "delete":
            cart.remove(product)

        return JsonResponse(
            {
                "success": True,
                "quantity": cart.cart.get(str(product_id), {}).get("quantity", 0),
                "total_count": cart.total_count,
            }
        )
    
class CartClearView(View): # Shouldn't they be generic.TemplateView
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()

        return JsonResponse({ "success": True, })



class CartDetailView(generic.TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = Cart(self.request)
        context["cart"] = cart

        return context


# need to be class-based
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, "cart/cart.html", {"cart": cart})


"""
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.cart.models import Cart


def cart_list(request):
    if request.method == 'GET':
        carts = list(Cart.objects.values())
        return JsonResponse(carts, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        cart = Cart.objects.create(
            user_id=data['user_id'],
            item=data['item'],
            quantity=data['quantity'],
            price=data['price']
        )
        return JsonResponse({'id': cart.id})

def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse({
            'user_id': cart.user_id,
            'item': cart.item,
            'quantity': cart.quantity,
            'price': cart.price,
            'added_at': cart.added_at
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        cart.item = data.get('item', cart.item)
        cart.quantity = data.get('quantity', cart.quantity)
        cart.price = data.get('price', cart.price)
        cart.save()
        return JsonResponse({'status': 'updated'})

    elif request.method == 'DELETE':
        cart.delete()
        return JsonResponse({'status': 'deleted'})
"""

# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from .models import Product
# from .cart import Cart
# from .forms import CartAddProductForm


# @require_POST
# def cart_add(request, product_id):
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)

#         cart.add(
#             product=product,
#             quantity=cd["quantity"],
#             update_quantity=cd["update"],  # Update part is not needed
#         )

#         response_data = {"success": True, "quantity": cd["quantity"]}
#         return JsonResponse(response_data)

#     # If form is not valid, return an error response
#     return JsonResponse({"success": False, "error": "Invalid form data"})


# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect("cart_detail")


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, "order.html", {"cart": cart})


# def order(request):
#     cart = Cart(request)
#     return render(request, "order.html", {"cart": cart})
