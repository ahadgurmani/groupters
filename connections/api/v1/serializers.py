from rest_framework import serializers

from connections.models import ConnectionRequests


class ConnectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequests
        fields = ['id', 'connection_to', 'connection_by', 'connection_status']