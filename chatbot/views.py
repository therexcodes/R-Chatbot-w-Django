from django.shortcuts import render
from .models import Chat
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Create your views here.
def chat_view(request):
    chat_history = Chat.objects.all().order_by('time_stamp')
    
    if request.method == 'POST':
        user_message = request.POST.get('message').lower()
        
        try:
            # Generate a response using the identified model
            response = openai.ChatCompletion.create(
                model="o1-preview",  # Replace with the model ID you want to test
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=150,
                temperature=0.7,
                top_p=0.9
            )
            
            # Extract the chatbot's response
            chatbot_response = response['choices'][0]['message']['content'].strip()
        
        except Exception as e:
            chatbot_response = f"An error occurred: {str(e)}"

        # Save the conversation to the database
        Chat.objects.create(bot_response=chatbot_response, user_text=user_message)
        chat_history = Chat.objects.all().order_by('time_stamp')

        return render(request, 'chat.html', {"chat_history": chat_history})

    return render(request, 'chat.html', {"chat_history": chat_history})
