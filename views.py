python -“# chatbot/views.py
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        if user_message:
            try:
                # Call OpenAI API
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
”