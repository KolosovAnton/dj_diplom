"""DJ_diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from DJ_diplom import settings
from cart.views import cart_add, cart_detail
from shop.views import home_view, show_page, UserRegisterView, UserLoginView, user_logout

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    url(r'^cart/add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    url(r'^cart/', cart_detail, name='cart_detail'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home_view, name='home'),
    url(r'^(?P<short_name>[\w-]+)/$', show_page, name='short_name'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
