from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import stripe
from django.views.generic import TemplateView
from django.conf import settings
from .models import Product
from django.views.decorators.csrf import csrf_exempt


from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


#Stripe Integration
stripe.api_key = settings.SECRET_KEY

def index(request):
    return render(request, 'landing.html')
#**********************************************************************************
#Stripe Checkout
@csrf_exempt
def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                # TODO: replace this with the `price` of the product you want to sell
                'price': 'price_1JpB9SSAkHUkLlU7ezdHz6BA',
                'quantity': 1,
            },
        ],


        mode='payment',
        success_url=request.build_absolute_uri(reverse('dash')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url= request.build_absolute_uri(reverse('index')),
    )


    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.PUBLIC_KEY
    })

#Stripe Webhook
@csrf_exempt
def stripe_webhook(request):
# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in the Developer Dashboard
  endpoint_secret = 'whsec_Giow1yoVvWVsDLHK5o9U4RqiXE4tuRXX'

  request_data = request.body
  signature = request.headers.get("stripe-signature")

  # Verify webhook signature and extract the event.
  # See https://stripe.com/docs/webhooks/signatures for more information.
  try:
    event = stripe.Webhook.construct_event(
        payload=request.body, sig_header=signature, secret=endpoint_secret
    )
  except ValueError as e:
    # Invalid payload.
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid Signature.
    return HttpResponse(status=400)

  if event["type"] == "checkout.session.completed":
    print("ihfighfhofshgoh")

    session = event["data"]["object"]



    print(session)
    line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
    print(line_items)

  return HttpResponse(status=200)



@csrf_exempt
def checkout2(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                # TODO: replace this with the `price` of the product you want to sell
                'price': 'price_1JmEqXSAkHUkLlU7f1h9YmgP',
                'quantity': 1,
            },
        ],

        mode='payment',
        success_url=request.build_absolute_uri(reverse('dash')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url= request.build_absolute_uri(reverse('index')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.PUBLIC_KEY
    })

#Stripe Checkout end************************************************************************************************


def registerPage(request):
# if request.user.is_authenticated:
#     return redirect('home')
# else:

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for ' + user)
    #
    #         return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def pay(request):
    return render(request, 'pay.html')



def dash(request):
    return render(request, 'dash.html')


