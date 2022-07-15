from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.SuperSerializer):
    class Meta:
        model = Super
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catachphrase', 'super_type']
