from django.urls import  path
from . import views
from .views import *
app_name = 'blog_app'

urlpatterns = [
    
    path('create/', PostCreateView.as_view(), name="create-post"),
    path('post_detail/<int:pk>',PostDetail.as_view(), name="post_details"),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post_delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('comment_count/<int:post_id>/<int:user_id>/', TotalCommentCountView.as_view(), name='comment-count'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view()),

    #Comments

    path('create_comment/', CommentCreateView.as_view(), name="create-comment"),
    path('comment_detail/<int:pk>',CommentDetail.as_view(), name="comment_details"),
    path('comment_update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment_delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete'),
    path('post_by_search/<int:post_id>/', PostWiseCommentListAPIView.as_view()),

    #Users Login & register

    path('users/', UserCreateView.as_view()),
    path('user_login/', UserLoginView.as_view()),
    path('usersearch/<str:username>/', UserSearchListAPIView.as_view()),
    path('user_by_search/<int:id>/', UserwiseListAPIView.as_view()),
    path('user_by_post/<int:id>/', UserWisePostListAPIView.as_view()),
    path('api/comment-count/', CommentCountAPIView.as_view(), name='comment-count'),

]
