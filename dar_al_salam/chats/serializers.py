""" Serializers for dar_al_salam.chats """

from rest_framework.serializers import ModelSerializer

from dar_al_salam.chats.models import Chat


# Create your serializers here.
class ChatSerializer(ModelSerializer):
    """Chat Serializer"""

    class Meta:
        """Meta Data"""

        model = Chat
        read_only_fields = ["from_user", "to_user"]
        fields = ["id", "url", "from_user", "to_user", "updated_at", "created_at"]