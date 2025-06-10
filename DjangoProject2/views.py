from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json

client = openai.OpenAI(api_key= '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')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

@csrf_exempt
def ai_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions about products."},
                    {"role": "user", "content": message}
                ]
            )

            reply = response.choices[0].message.content
            return JsonResponse({'reply': reply})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)