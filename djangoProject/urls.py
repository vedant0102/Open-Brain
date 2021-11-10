from django.contrib import admin
from django.urls import path
from payment import views as pay
from register import views as reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pay.index, name='index'),
    path('checkout/', pay.checkout, name='checkout'),
    path('checkout2/', pay.checkout2, name='checkout2'),
    path('stripe_webhook/', pay.stripe_webhook, name='stripe_webhook'),
    path('pay/', pay.pay, name='pay'),
    path('dash/', pay.dash, name='dash'),
    path('register/', pay.registerPage, name="register"),



    path('login/', reg.login,name="login")



]
