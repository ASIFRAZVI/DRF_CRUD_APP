from .models import crudobj
from rest_framework import serializers

class crud_serializer(serializers.ModelSerializer):
    class Meta:
        model=crudobj
        fields='__all__'
        