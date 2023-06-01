from django.contrib import admin
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from user import views

urlpatterns = [
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/dj-rest-auth/registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),  # Needs to be defined before the registration path
    path(
        "api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")
    ),
    path(
        "api/v1/dj-rest-auth/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "api/v1/dj-rest-auth/password/change/",
        PasswordChangeView.as_view(),
    ),
    path("api/v1/dj-rest-auth/password/reset/", PasswordResetView.as_view()),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("api/v1/password/forgot/", views.forgot_password),
    path("api/v1/password/forgot/change/", views.change_password_on_secret),
]
