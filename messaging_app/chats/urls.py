from django.urls import include, path
from rest_framework import routers
from .views import MessageViewSet, ConversationViewSet

router = routers.DefaultRouter()
router.register(r'messages',  MessageViewSet, basename='')
router.register(r'conversations', ConversationViewSet, basename='conversation')

conversations_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversations_router(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls))
    path('', include(conversations_router.urls))
]
