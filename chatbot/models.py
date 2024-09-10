from django.db import models

# Create your models here.
class Chat(models.Model):
    user_text = models.CharField(max_length=1000)
    bot_response = models.CharField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    # displaying the  User and bot conversation in the DB
    def __str__(self):
        return f"User: {self.user_text} & Bot_reply: {self.bot_response}"