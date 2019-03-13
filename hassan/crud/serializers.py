from rest_framework import serializers
from crud.models import Crud

class CrudSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField(required=False, allow_blank=True, max_length=20)
    class Meta:
        model = Crud
        fields = ('id', 'purchase', 'purchase_id', 'user_id', 'name', 'phone_number', 'email', 'address','date_time')

#Crudserializer.is_valid()
#erializer.errors


