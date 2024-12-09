

# Blogging application  
Develop a fully functional, blogging website with user authentication. The website should
allow registered users to create, edit, and delete blog posts while providing a secure and
intuitive user experience.

Technologies Used: HTML, CSS, Bootstrap,Javascript, Django Rest Framework, Postressql

Table of Contents
Project Overview
Prerequisites
Installation
Configuration
Database Setup
API Endpoints
Authentication
Testing
Project Structure
Contributing
License
Project Overview

This DRF project aims to provide a RESTful API for managing data in a Django application. The API supports common operations such as User Authentication, Authorization, Guest Access. It is designed to be scalable and easy to extend.

Prerequisites
Before setting up the project, ensure that you have the following installed:

Python (3.x)
Django (>= 3.2)
Django Rest Framework (>= 3.12)

# You can install these prerequisites using:

pip install Django==3.2
pip install djangorestframework==3.12
Installation
Clone the repository:

# Copy code
# cd <repository-name>
# Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # For Unix/Mac
# For Windows
venv\Scripts\activate.bat

# Install the project dependencies:

pip install -r requirements.txt

# Migrate the database:
python manage.py migrate

# Run the development server:

python manage.py runserver

Now, you should be able to view the application at http://127.0.0.1:8000.

Configuration
Configure any necessary settings by updating the settings.py file. Modify the database configurations, static file settings, and other environment-specific variables as needed.

#Database Setup
Uses postgressql database to store the blog data

# API Endpoints
The DRF project exposes the following API endpoints:

# Posts
Create Blog Post:

Endpoint: path('create/', PostCreateView.as_view(), name="create-post")
Description: Create a new blog post.
Post Detail:

Endpoint: path('post_detail/<pk>')
Description: Retrieve details of a specific post instance by its ID.
Update Post:

Endpoint: path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post-update')
Description: Update an existing blog post by its ID.
Delete Post:

Endpoint: path('post_delete/<int:pk>/', PostDelete.as_view(), name='post_delete')
Description: Delete a blog post by its ID.
Total Comment Count:

Endpoint: path('comment_count/<int:post_id>/<int:user_id>/', TotalCommentCountView.as_view(), name='comment-count')
Description: Get the total number of comments for a specific post and user.
Delete Post (alternative URL):

Endpoint: path('post/<int:pk>/delete/', views.PostDelete.as_view())
Description: Alternative URL for deleting a blog post.

# Comments

Create Comment:

Endpoint: path('create_comment/', CommentCreateView.as_view(), name="create-comment")
Description: Create a new comment on a blog post.
Comment Detail:

Endpoint: path('comment_detail/<int:pk>')
Description: Retrieve details of a specific comment by its ID.
Update Comment:

Endpoint: path('comment_update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update')
Description: Update an existing comment by its ID.
Delete Comment:

Endpoint: path('comment_delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete')
Description: Delete a comment by its ID.
Post by Search:

Endpoint: path('post_by_search/<int:post_id>/', PostWiseCommentListAPIView.as_view())
Description: Get comments for a specific post by its ID.

# Users

User Registration:

Endpoint: path('users/', UserCreateView.as_view())
Description: Register a new user.
User Login:

Endpoint: path('user_login/', UserLoginView.as_view())
Description: Log in a user.
User Search:

Endpoint: path('usersearch/<str:username>/', UserSearchListAPIView.as_view())
Description: Search for users by username.
User by ID:

Endpoint: path('user_by_search/<int:id>/', UserwiseListAPIView.as_view())
Description: Get user details by ID.
User by Post:

Endpoint: path('user_by_post/<int:id>/', UserWisePostListAPIView.as_view())
Description: Get posts by a specific user ID.
Comment Count:

Endpoint: path('api/comment-count/', CommentCountAPIView.as_view(), name='comment-count')
Description: Get the count of comments.



# Authentication
The project uses session-based authentication with Django Rest Framework’s TokenAuthentication class. To generate a token, make a POST request to the /auth/token/ endpoint with your credentials. You will receive a token that can be used for subsequent requests.

# Testing
The project includes unit tests to verify API functionality. You can run tests using:


# python manage.py test

Project Structure
apps/: Contains all the Django apps used in the project.
migrations/: Holds database migration files.
static/: Static files like CSS, JavaScript, images, etc.
templates/: Django templates.
requirements.txt: Lists all the dependencies required for the project.
manage.py: Django’s command-line utility for administrative tasks.
urls.py: Defines the URL configuration for the project.
settings.py: Project settings.

