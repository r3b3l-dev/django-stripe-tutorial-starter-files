from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView
)
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checout-session'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
