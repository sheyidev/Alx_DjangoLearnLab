## Objective: 

Start building a Social Media API from scratch, focusing on setting up the project environment, user authentication, and creating the initial user models.

## Task Description:
Begin by establishing the foundational elements of your Social Media API. This includes setting up the Django project, integrating Django REST Framework for API functionality, and implementing a robust user authentication system.

**Step 1: Create a New Django Project**
- Environment Setup:
   - Install Django and Django REST Framework using pip, if not already installed: bash pip install django djangorestframework
   - Create a new Django project named social_media_api: bash django-admin startproject social_media_api
   - Navigate into your project directory and create a new Django app called accounts for handling user-related functionality: bash cd social_media_api python manage.py startapp accounts
   - Add 'rest_framework' and 'accounts' to the INSTALLED_APPS in settings.py.

**Step 2: Configure User Authentication**

- User Model and Authentication:
   - Create a custom user model that extends Django’s AbstractUser, adding fields such as bio, profile_picture, and followers (a ManyToMany field referencing itself, symmetrical=False).
   - Set up Django REST Framework’s token authentication by adding 'rest_framework.authtoken' to your installed apps and running migrations to create the token model.
   - Implement views and serializers in the accounts app for user registration, login, and token retrieval.

**Step 3: Define URL Patterns**
   - Routing Configuration:
        - Configure URL patterns in accounts/urls.py to include routes for registration (/register), login (/login), and user profile management (/profile).
        - Ensure that registration and login endpoints return a token upon successful operations.
        
**Step 4: Testing and Initial Launch**
- Server Testing:
    - Start the Django development server to ensure the initial setup is configured correctly: bash python manage.py runserver
    - Use tools like Postman to test user registration and login functionalities, verifying that tokens are generated and returned correctly.

**Deliverables:**
1. **Project Setup Files:** Include all configuration files, initial migrations, and the Django project structure.
2. **Code Files:** Include models, views, and serializers for the user authentication system in the `accounts` app.
3. **Documentation:** Provide a README file detailing the setup process, how to register and authenticate users, and a brief overview of the user model.
Repo:

- GitHub repository: `Alx_DjangoLearnLab`
- Directory: `social_media_api`

##



## Implementing Posts and Comments Functionality

**Objective:** Develop core functionalities of the Social Media API by adding posts and comments features. This task will enable users to create, view, update, and delete posts and comments within the social media platform.

**Task Description:**

Expand your `social_media_api` project by creating functionality for users to manage posts and engage with them through comments. This includes setting up models, serializers, views, and routes for posts and comments.

Step 1: Create Post and Comment Models

- **Model Definitions:**

    - In a new app within the project called posts, create models for Post and Comment.
    - Post should have fields like author (ForeignKey to User), title, content, created_at, and updated_at.
    - Comment should reference both Post (ForeignKey) and User (author), with additional fields for content, created_at, and updated_at.


- **Database Setup:**

   - Include these models in your migrations and update the database by running: bash python manage.py makemigrations posts python manage.py migrate


**Step 2: Implement Serializers for Posts and Comments**
- Serializer Setup:
   - Create serializers for both `Post` and `Comment` in `posts/serializers.py.`
   - Ensure that serializers handle user relationships correctly and validate data as needed.

**Step 3: Create Views for CRUD Operations**
- **View Implementation:**
    - Using Django REST Framework’s viewsets, set up CRUD operations for both posts and comments in posts/views.py.
    - Implement permissions to ensure users can only edit or delete their own posts and comments.

**Step 4: Configure URL Routing**

**Routing Configuration:**

   - Define URL patterns in posts/urls.py that map to the viewsets using Django REST Framework’s routers. This includes routes for listing, creating, editing, and deleting both posts and comments.


**Step 5: Implement Pagination and Filtering**

**Enhance API Usability:**
   - Add pagination to post and comment list endpoints to manage large datasets.
   - Implement filtering capabilities in post views to allow users to search posts by title or content.

**Step 6: Test and Validate Functionality**

Testing Guidelines:

- Thoroughly test all endpoints using tools like Postman or automated tests to ensure they behave as expected.
- Validate that permissions are correctly enforced and that data integrity is maintained through the API.

**Step 7: Document API Endpoints**

**Documentation:**

- Update the API documentation to include detailed information on how to interact with the posts and comments endpoints.
- Provide examples of requests and responses for all operations.

**Deliverables:**

1. Code Files: Include all models, serializers, views, and URL configurations related to posts and comments.
2. API Documentation: Detailed descriptions of each endpoint, including usage examples.
3. Testing Results: Evidence of testing and validation, including any scripts or Postman collections used.


`Repo:`

GitHub repository: `Alx_DjangoLearnLab`

Directory: `social_media_api`