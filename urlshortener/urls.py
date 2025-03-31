from django.contrib import admin
from django.urls import path
from shortener.views import home, redirect_short_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<str:short_code>/', redirect_short_url, name='redirect_short_url'),
]
