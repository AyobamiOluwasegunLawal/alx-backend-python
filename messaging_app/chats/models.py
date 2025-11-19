import uuid
from django.db import models
from django.contrib.auth.models import AbstactUser

# Create your models here.
class User(AbstactUser):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    phone_number = models.CharField(
        max_length=20, 
        null=True, 
        blank=True
    )

    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='guest'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD =  []

class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True
    )

    participants_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='conversations'
    )

    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    sender_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

