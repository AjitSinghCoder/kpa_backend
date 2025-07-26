# How to Run with Docker

## Quick Start

1. **Start the project:**
   ```bash
   docker-compose up --build
   ```

2. **Setup database (IMPORTANT - Run this after first startup):**
   ```bash
   docker-compose exec web sh -c "python manage.py makemigrations forms && python manage.py migrate"
   ```

3. **Open in browser:**
   - API: http://localhost:8000
   - Admin: http://localhost:8000/admin
   - Docs: http://localhost:8000/swagger/

4. **Stop the project:**
   ```bash
   docker-compose down
   ```
