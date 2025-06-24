from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import logging
from django.shortcuts import render
logger = logging.getLogger(__name__)

OPENROUTER_API_KEY = "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"

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


def preview_360(request):
    return render(request, 'product_360.html')

@csrf_exempt
def ai_chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message')

            if not user_input:
                return JsonResponse({'error': 'Mesajul este gol.'}, status=400)

            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",  # sau domeniul tău real
                "X-Title": "Fiare din Beci Assistant"
            }

            payload = {
                "model": "mistralai/mistral-7b-instruct",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that answers questions about handmade knives, blades, and custom orders."},
                    {"role": "user", "content": user_input}
                ]
            }

            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

            if response.status_code != 200:
                print("Status code:", response.status_code)
                print("Response text:", response.text)
                return JsonResponse({'error': 'Eroare de la OpenRouter'}, status=500)

            result = response.json()

            try:
                reply = result['choices'][0]['message']['content']
            except Exception as e:
                print("Eroare în parsare:", str(e))
                print("Răspuns complet:", result)
                return JsonResponse({'error': 'Format de răspuns invalid.'}, status=500)

            return JsonResponse({'reply': reply})

        except Exception as e:
            print("Eroare generală:", str(e))
            return JsonResponse({'error': 'Eroare internă.'}, status=500)

    return JsonResponse({'error': 'Doar POST este acceptat.'}, status=405)


