📝 Personal Blog API
A RESTful API for a personal blogging platform, built with Python Flask. This project provides secure endpoints for user authentication, blog post management, and commenting, all protected with JWT. It follows a modular architecture using Flask Blueprints, integrates Marshmallow for validation, and employs robust error handling, logging, and database management using Flask-SQLAlchemy.

🚀 Features
🔐 User Authentication

Register, login, and manage user profiles using JWT authentication.

📝 Blog Posts

Create, Read, Update, and Delete (CRUD) blog posts.

Only authenticated users can perform write operations.

💬 Comments

Add and view comments on blog posts.

Comment creation is restricted to authenticated users.

🧱 Modular Architecture

Scalable structure using Flask Blueprints:

auth/ – User authentication and profile

posts/ – Blog post routes

comments/ – Comment-related operations

✅ Request Validation

Input validation and serialization with Marshmallow schemas.

💾 Database Management

ORM with Flask-SQLAlchemy

SQLite for development, ready for PostgreSQL in production.

Version control with Flask-Migrate

⚠️ Error Handling

Centralized and consistent error responses.

📜 Logging

Logs requests, errors, and application events using Python Logging.

🔧 Environment Configuration

Manage environment variables using python-dotenv.

