# FastAPI Secure File Sharing System - Setup Guide

This guide provides instructions on setting up and running the FastAPI Secure File Sharing System. Follow the steps below to get started.
Prerequisites

# Before you begin, make sure you have the following installed:
```
    Python 3.7 or later
    FastAPI (install using pip install fastapi)
    Uvicorn (install using pip install uvicorn)
    Pydantic (install using pip install pydantic)
```
# Clone the Repository
```
    git clone https://github.com/your-username/fastapi-secure-file-sharing.git
    cd fastapi-secure-file-sharing
```

# Setup Virtual Environment (Optional but Recommended)
```
    python -m venv venv
    # On Windows: .\venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
```

# Install Dependencies
```
    pip install -r requirements.txt
```

# Configure Environment Variables

Create a .env file in the root of the project and configure is according to env.example file. You can use the following command to create the file:

# Run the Application
```
    uvicorn main:app --reload
```
The application will be accessible at http://127.0.0.1:8000 by default.

# API Documentation

Once the application is running, you can access the interactive API documentation at http://127.0.0.1:8000/docs and the alternative Swagger UI at http://127.0.0.1:8000/redoc. These tools provide a detailed overview of the available endpoints and allow you to test the API directly.

