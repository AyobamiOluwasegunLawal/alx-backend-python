from django.shortcuts import render
from rest_framework import permissions, viewsets, status, filters
from .serializers import ConversationSerializer, MessageSerializer
from .models import Message, Conversation
# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        return Conversation.objects.filter(
            participants_id = self.request.user
        ).order_by('-created_at')

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        return Message.objects.filter(
            send_id = self.request.user
        ).order_by('-sent_at')