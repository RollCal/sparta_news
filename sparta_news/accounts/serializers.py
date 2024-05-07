from rest_framework import serializers
from .models import User
from .models import spartanews  

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['first_name','last_login',"is_superuser",'last_name','is_staff','is_active','date_joined','groups','user_permissions']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = spartanews
        fields = ['id', 'title', 'content', 'created_at'] 