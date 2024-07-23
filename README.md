# Blog Webapp Back-end

This is the back-end for our blog webapp, built using Django REST Framework.

## Getting Started

[Installation and setup instructions remain the same]

## API Endpoints

### User Management
- `/users/`: User management endpoints (refer to user app for specific endpoints)

### Blog Operations
- `/blog/`: Create a new blog post
- `/blog/list`: Get a list of all blog posts
- `/blog/<int:id>`: Update a specific blog post
- `/blog/list/<int:id>`: Retrieve details of a specific blog post
- `/blog/image-upload`: Upload an image for a blog post

### Authentication
- `/api/token/`: Obtain JWT token
- `/api/token/refresh/`: Refresh JWT token

### Admin and Documentation
- `/admin/`: Django admin interface
- `/swagger/`: Swagger UI for API documentation
- `/redoc/`: ReDoc UI for API documentation
- `/swagger.json`: OpenAPI specification in JSON format

## Features

- RESTful API for blog posts and user management
- CRUD operations for blog posts
- Image upload functionality for blog posts
- User authentication using JWT (JSON Web Tokens)
- Django admin interface for easy management
- Swagger/OpenAPI documentation
- Permissions and authentication for protected routes

## API Documentation

We use Swagger/OpenAPI for API documentation. You can access the documentation through the following endpoints:

- Swagger UI: `/swagger/`
- ReDoc UI: `/redoc/`
- OpenAPI JSON: `/swagger.json`

These interfaces provide detailed information about all available endpoints, request/response formats, and allow for interactive API testing.

## Project Structure

```
blog_project/
  ├── user/
  │   └── urls.py
  ├── blog/
  │   ├── urls.py
  │   └── views.py
  ├── blog_project/
  │   ├── settings.py
  │   └── urls.py
  ├── manage.py
  └── requirements.txt
```

Key components:
- `user`: Handles user management
- `blog`: Manages blog post functionality
  - `urls.py`: Defines the URL patterns for blog operations
  - `views.py`: Contains view classes like BlogCreationView, BlogPostListView, etc.
- `blog_project`: Main project directory with settings and root URL configuration

## Blog App Views

The `blog` app includes the following main views:
- `BlogCreationView`: Handles creation of new blog posts
- `BlogPostListView`: Retrieves a list of all blog posts
- `BlogUpdateView`: Allows updating of existing blog posts
- `BlogPostRetrievalView`: Retrieves details of a specific blog post
- `ImageUploadView`: Handles image uploads for blog posts

## Third-party Libraries

- Django REST Framework: For building the RESTful API
- Simple JWT: For JWT authentication
- drf-yasg: For Swagger/OpenAPI documentation

