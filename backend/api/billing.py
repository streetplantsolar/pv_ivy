import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscribeView(APIView):
    def post(self, request):
        user = request.user
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{'price': settings.STRIPE_PRICE_ID, 'quantity': 1}],
                mode='subscription',
                success_url=settings.FRONTEND_URL + '/dashboard',
                cancel_url=settings.FRONTEND_URL + '/billing'
            )
            return JsonResponse({'sessionId': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
