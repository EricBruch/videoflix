from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import CustomUser
from .utils import change_password
import random
import string

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def forgot_password(request):
    try:
        user = CustomUser.objects.get(username=request.data["username"])

        resetSecret = "".join(random.choices(string.ascii_letters, k=20))
        user.resetSecret = resetSecret

        send_mail(
            "Forgot password service",
            "Your shared secret to reset your password is: " + resetSecret,
            "support@example.com",
            [user.email],
            fail_silently=False,
        )
        user.save()
    except Exception as e:
        print("Error occured: ", e)
    finally:
        return Response({"message": "executed successfully"})


@api_view(["POST"])
@permission_classes([AllowAny])
def change_password_on_secret(request):
    # user = CustomUser.objects.get(username="troja")
    # user.set_password("okfhgzrkfkfkfrkfj")
    # user.save()
    # return Response({"message": "executed successfully"})
    try:
        username, pw1, pw2, secret = (
            request.data["username"],
            request.data["newPassword1"],
            request.data["newPassword2"],
            request.data["sharedSecret"],
        )
        change_password(username, pw1, pw2, secret)
    except Exception as e:
        print("Error occured: ", e)
    finally:
        return Response({"message": "executed successfully"})
