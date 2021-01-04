from rest_framework import serializers

class NodeSerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lng = serializers.FloatField(required=True)