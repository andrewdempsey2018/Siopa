from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from django.http import JsonResponse

import stripe
# move this to Heroku settings
stripe.api_key = 'sk_test_bQtVOCRPhqEfuCsRbJuSA5cz00KG7oSgPU'


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


DOMAIN = 'http://localhost:8000'


@csrf_exempt
def create_checkout_session(self):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'EUR',
                        'unit_amount': 500,
                        'product_data': {
                            'name': 'Plant Pot',
                            'images': ['https://images4-g.ravelrycache.com/uploads/dayana/216912709/close_up_rowan_small2.jpg'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/success',
            cancel_url=DOMAIN + '/cancel',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse(error=str(e)), 403
