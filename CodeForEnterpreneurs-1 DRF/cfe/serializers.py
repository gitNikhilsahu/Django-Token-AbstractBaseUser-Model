from rest_framework import serializers

class CFESerializer(serializers.Serializer):
    title = serializers.CharField(max_length=10)
