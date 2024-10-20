from django.shortcuts import render
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = 'your-openai-api-key'  # Replace with your actual API key

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        if user_message:
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=user_message,
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.7,
                )

                bot_message = response.choices[0].text.strip()
                return JsonResponse({'bot_response': bot_message}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Create your views here.
