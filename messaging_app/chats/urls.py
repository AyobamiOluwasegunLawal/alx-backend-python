from django.urls import include, path
from rest_framework import routers
from .views import MessageViewSet, ConversationViewSet

router = routers.DefaultRouter()
router.register(r'messages',  MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
