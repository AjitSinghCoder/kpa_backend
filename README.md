# KPA Backend


## Features

- **Wheel Specification Management**: Create and retrieve wheel specification forms
- **Advanced Filtering**: Filter specifications by form number, submitted by, and submission date
- **Pagination**: Built-in pagination for efficient data handling
- **API Documentation**: Interactive Swagger/OpenAPI documentation
- **PostgreSQL Database**: Robust database backend with JSON field support
- **CORS Support**: Cross-origin resource sharing enabled
- **Environment Configuration**: Secure environment-based configuration

## Tech Stack

- **Framework**: Django 5.2.4
- **API**: Django REST Framework 3.16.0
- **Database**: PostgreSQL with psycopg2-binary 2.9.10
- **Documentation**: drf-yasg 1.21.10 (Swagger/OpenAPI)
- **CORS**: django-cors-headers 4.7.0
- **Environment**: python-dotenv 1.1.1

## Project Structure

```
kpa_backend/
├── forms/                  # Main application for wheel specifications
│   ├── models.py          # WheelSpecification model
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # URL routing
│   └── migrations/        # Database migrations
├── kpa_backend/           # Project configuration
│   ├── settings/     
│   │   ├── base.py        # Base settings
│   │   ├── dev.py         # Development settings
│   │   └── prod.py        # Production settings
│   ├── urls.py            # Main URL configuration
│   ├── swagger.py         # Swagger configuration
│   └── wsgi.py            # WSGI configuration
├── utils/                 # Utility modules
│   └── response.py        # Custom response utilities
├── requirements.txt       # Python dependencies
├── sample.env            # Environment variables template
└── manage.py             # Django management script
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kpa_backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp sample.env .env
   ```

   Edit `.env` file with your configuration:
   ```env
   DEBUG=True
   SECRET_KEY="your-secret-key-here"
   DB_NAME=kpa_backend
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Database Setup**
   ```bash
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Documentation

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/swagger/`

## API Admein
`http://localhost:8000/admin`