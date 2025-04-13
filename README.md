Personal Blog API
A RESTful API for a personal blog built with Python Flask. This project provides endpoints for user authentication, blog post management, and comments, secured with JWT authentication. It features a modular boilerplate structure using Blueprints, request validation with Marshmallow, robust error handling, logging, and database management with Flask-SQLAlchemy.

Features
User Authentication: Register, login, and view user profiles using JWT.
Blog Posts: Create, read, update, and delete (CRUD) blog posts, restricted to authenticated users for write operations.
Comments: Add and view comments on posts, with authentication for comment creation.
Modular Structure: Organized with Flask Blueprints for scalability (auth, posts, comments).
Request Validation: Uses Marshmallow for input validation and serialization.
Database: Managed with Flask-SQLAlchemy (SQLite for development, PostgreSQL-ready for production).
Error Handling: Centralized error responses for consistent API behavior.
Logging: Logs requests, errors, and key events for debugging and monitoring.
Tech Stack
Flask: Lightweight Python web framework.
Flask-SQLAlchemy: ORM for database interactions.
Flask-JWT-Extended: JWT-based authentication.
Marshmallow: Request/response validation and serialization.
Flask-Migrate: Database migrations.
Python Logging: For request and error logging.
python-dotenv: Environment variable management.