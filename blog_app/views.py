from django.shortcuts import render, redirect

from .forms import PostForm, CreateUserForm, LoginForm, CreateCommentForm
from. serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import requests
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Count  

# Create your Api here.



class UserCreateView(generics.ListCreateAPIView):
    queryset = UsersDetails.objects.all()
    serializer_class = CreateUserSerializers
    permission_classes = [AllowAny]
    

class UserLoginView(generics.ListAPIView):
    queryset = UsersDetails.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')  # Use request.data for POST requests
        password = request.data.get('password', '')

        users = UsersDetails.objects.filter(username=username, password=password)

        if users.exists():
            user = users.first()  # Retrieve the first user from the queryset
            serializer = self.serializer_class(user)  # Use the serializer class directly
            return Response({'message': 'Login Successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserSearchListAPIView(generics.RetrieveAPIView):
    serializer_class = CreateUserSerializers
    queryset = UsersDetails.objects.all()

    def get_object(self):
        username = self.kwargs.get('username')  # Retrieve 'username' from URL kwargs
        return UsersDetails.objects.get(username=username)
    
class UserwiseListAPIView(generics.RetrieveAPIView):
    serializer_class = CreateUserSerializers
    queryset = UsersDetails.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('id')  # Retrieve 'username' from URL kwargs
        return UsersDetails.objects.get(id=user_id)
    
class UserWisePostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializers

    def get_queryset(self):
        post_id = self.kwargs['id']
        return Post.objects.filter(author_id=post_id)      
    
 #-------------------------------------------------- Blog Post API----------------------------------------------------------------------   
        

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Order posts by ID in ascending order
        return Post.objects.order_by('-id')
    
#API Fetching post data based on a particular id

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_extra_actions(self):
        return [] 
    

class PostUpdateView(generics.RetrieveUpdateAPIView):
     
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_extra_actions(self):
        return []

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_extra_actions(self):
        return []    
    
class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers 


class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [AllowAny]

    def get_extra_actions(self):
        return []
    
#API Fetching recipes data based on a particular id

class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get_extra_actions(self):
        return []     

class CommentUpdateView(generics.RetrieveUpdateAPIView):
     
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get_extra_actions(self):
        return []

class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get_extra_actions(self):
        return []            
    
class PostWiseCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializers

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)   

class TotalCommentCountView(APIView):
    def get(self, request, user_id, post_id):
        # Attempt to get the post object by ID
        try:
            post = Post.objects.filter(author_id=user_id).count()
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        # Count the comments related to this post using the post_id
        total_comment_count = Comment.objects.filter(user=user_id).count()
        comment_count = Comment.objects.filter(user=user_id, post=post_id).count()
        
        return Response({'post_count': post, 'total_comment_count': total_comment_count, 'comment_count':comment_count})


class CommentCountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Aggregate comments for each post
        comment_counts = (
            Comment.objects.filter(post__in=Post.objects.all())
            .values('post')
            .annotate(comment_count=Count('id'))
            .order_by('-post')  # Order by post ID in descending order
        )
        
        # Format the data
        data = [
            {"post_id": item['post'], "comment_count": item['comment_count']}
            for item in comment_counts
        ]
        
        return Response(data, status=status.HTTP_200_OK)