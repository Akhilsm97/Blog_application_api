from datetime import timedelta
from .models import *
from rest_framework import serializers

class PostSerializers(serializers.ModelSerializer):
    blog_image = serializers.ImageField(required=False) # Set required to False for the image field

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class CreateUserSerializers(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model = UsersDetails
        fields = '__all__'    
            
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'       


