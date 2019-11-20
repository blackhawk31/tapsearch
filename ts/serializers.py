from rest_framework import serializers

from .models import Index

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['document_id','key','frequency']