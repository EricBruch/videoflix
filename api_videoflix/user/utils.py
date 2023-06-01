from django.core.mail import send_mail
from .models import CustomUser
import random
import string


def change_password(username, pw1, pw2, secret):
    if pw1 != pw2:
        raise Exception("pw1 not equal to pw2")

    user = CustomUser.objects.get(username=username)

    if user.resetSecret != secret:
        raise Exception("secret not correct")

    user.set_password(pw1)

    send_mail(
        "Your password was changed successfully",
        "Your password was resetted successfully",
        "support@example.com",
        [user.email],
        fail_silently=False,
    )

    user.resetSecret = "".join(random.choices(string.ascii_letters, k=20))
    user.save()
