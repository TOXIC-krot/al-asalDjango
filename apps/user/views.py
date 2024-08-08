import json
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from .models import User


def check_user(request):
    user_id = request.GET.get("user_id")
    if user_id:
        exists = User.objects.filter(user_id=user_id).exists()
        return JsonResponse({"exists": exists})
    return JsonResponse({"exists": False}, status=400)


@csrf_exempt
def update_last_active(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get("user_id")
        print(f"the user's id is {user_id}")
        if user_id:
            user = User.objects.filter(user_id=user_id).first()
            if user:
                user.save()  # This will update the `last_active_at` field
                return JsonResponse({"status": "success"})
        return JsonResponse(
            {"status": "error", "message": "Invalid user ID"}, status=400
        )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=405
    )


@csrf_exempt
def save_user_info(request):
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Invalid request method"}, status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON data"}, status=400
        )

    if (
        not data.get("user_id") or not data.get("phone_number") or not data.get("token")
    ):  # is it enough to not be null
        return JsonResponse(
            {"status": "error", "message": "Missing required fields"}, status=400
        )

    """
    user, created = User.objects.get_or_create(user_id=user_id, defaults={
        'username': data.get('username'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'phone_number': data.get('phone_number')
    })
    if not created:  # actually it always be not created
        user.username = data.get('username')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.phone_number = data.get('phone_number')
        # user.save()   WAS REMOVED
    """

    user = User.objects.create(
        user_id=data.get("user_id"),
        username=data.get("username"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        phone_number=data.get("phone_number"),
        token=data.get("token"),
    )

    return JsonResponse({"status": "success"})


def token_login(request):
    token = request.GET.get("token")
    user = get_object_or_404(User, token=token)
    user.token = None  # Clear the token after login
    user.save()
    try:
        login(request, user)
    except Exception as e:
        print("EXCEPTION OCCURRED", e)
    return redirect("product_list")  # Redirect to the desired page after login
