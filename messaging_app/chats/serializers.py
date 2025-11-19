from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    message_body = serializers.CharField(max_length=500)

    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    messages = MessageSerializer(many=True, read_only=True, source='message_set')
    last_messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = '__all__'

    def get_last_message(self, messagePayload):
        last_msg = messagePayload.message_set.order_by('-sent_at').first()
        return last_msg.message_body if last_msg else None
    
    def validate(self, data):
        participants = data.get('participants_id')

        if not participants or len(participants) < 2:
            raise serializers.ValidationError(
                "A conversation must have at least 2 participants."
            )
        return data
