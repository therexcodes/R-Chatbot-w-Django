from django.shortcuts import render, redirect
from .models import Chat
from datetime import datetime
import re




# Create your views here.
def chat_view(request):
    chat_history = Chat.objects.all().order_by('time_stamp')
    
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        user_message = user_message.lower()
        
        if user_message in ["hello", "hi", "hey"]:
            response = "Hello! How can I assist you today?"
        elif user_message in ["how are you", "how's it going", "what's up"]:
            response = "I'm just a bot, but I'm doing great! How can I help you?"
        elif user_message in ["what is your name", "who are you", "tell me about yourself"]:
            response = "I am ChatBot, here to help with your questions."
        elif user_message in ["bye", "goodbye", "see you later"]:
            response = "Goodbye! Have a wonderful day!"
        elif user_message in ["what time is it", "current time", "tell me the time", "what is th time", "time"]:
            now = datetime.now()
            response = f"The current time is {now.strftime('%H:%M:%S')}."
        elif user_message in ["date", "today's date", "what is the date", "what date is it"]:
            today = datetime.now()
            response = f"Today's date is {today.strftime('%Y-%m-%d')}."
        elif user_message in ["weather", "what's the weather like", "current weather"]:
            response = "I'm sorry, I can't check the weather. Please use a weather app or website."
        elif user_message in ["joke", "tell me a joke", "make me laugh"]:
            response = "Why don’t scientists trust atoms? Because they make up everything!"
        elif user_message in ["fact", "tell me a fact", "give me a fact"]:
            response = "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
        elif user_message in ["news", "what's the news", "latest news"]:
            response = "I don't have real-time news access. Please check a news website or app for the latest updates."
        elif user_message in ["help", "can you help me", "assistance"]:
            response = "Of course! What do you need help with? Feel free to ask me anything."
        elif user_message in ["math", "calculate", "do some math"]:
            response = "I can help with basic math. For example, you can ask me to add, subtract, multiply, or divide numbers."
        elif user_message.startswith("calculate"):
            # Extract mathematical expression from the user message
            expression = re.sub(r"calculate\s+", "", user_message)
            try:
                # Evaluate the expression
                result = eval(expression)
                response = f"The result of {expression} is {result}."
            except Exception as e:
                response = "Sorry, I couldn't calculate that. Please check your expression and try again."
        else:
            response = "I'm not sure how to respond to that. Could you please rephrase your question?"

        Chat.objects.create(bot_response = response, user_text = user_message)

        return redirect('chat_view')
    
    else:
        return render(request, 'chat.html', {"chat_history": chat_history})