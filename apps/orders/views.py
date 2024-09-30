from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem
import json

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Получаем данные из запроса
            products = data['products']
            total_price = data['totalPrice']

            # Создаем новый заказ (дополните логику согласно вашим моделям)
            order = Order.objects.create(user=None)  # Замените `None` на реального пользователя
            for product in products:
                OrderItem.objects.create(
                    order=order,
                    product_id=product,  # предполагаем, что передается ID продукта
                    price=total_price,  # Логика расчета цены за товар
                    count=1  # Замените на нужное количество
                )
            return JsonResponse({"message": "Order created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)