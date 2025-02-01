# Multilingual FAQ System

A Django-based FAQ management system with automatic translation support for Hindi and Bengali, built with Django REST Framework and Redis caching.

## Features

- ✨ Multilingual support (English, Hindi, Bengali)
- 🔄 Automatic translation using Google Translate
- 💾 Redis-based caching for improved performance
- 🎨 Rich text editing with CKEditor
- 🔐 Django Admin interface for content management
- 🚀 REST API endpoints for FAQ retrieval
- 📱 Mobile-friendly API responses

## Tech Stack

- Django 5.1
- Django REST Framework
- Redis (for caching)
- CKEditor
- Google Translate API
- SQLite (can be configured for other databases)

## Prerequisites

- Python 3.8+
- Redis Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd faq-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework django-ckeditor redis django-redis python-dotenv googletrans==3.1.0a0
```

4. Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://127.0.0.1:6379/0
```

5. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the Redis server:
```bash
redis-server
```

8. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
faq_system/
├── faqs/
│   ├── admin.py          # Admin interface configuration
│   ├── models.py         # FAQ model with translation support
│   ├── serializers.py    # API serializers
│   └── views.py          # API views with caching
├── faq_system/
│   ├── settings.py       # Project settings
│   └── urls.py           # URL configurations
└── manage.py
```

## API Endpoints

### Get FAQ List
- `GET /api/faqs/`
- Optional query parameter: `lang` (hi/bn)
- Example: `GET /api/faqs/?lang=hi` for Hindi translations

### Get Single FAQ
- `GET /api/faqs/<id>/`
- Optional query parameter: `lang` (hi/bn)
- Example: `GET /api/faqs/1/?lang=bn` for Bengali translation

### Create FAQ (Admin only)
- `POST /api/faqs/`
- Requires authentication
- Automatically translates content to Hindi and Bengali

### Update FAQ (Admin only)
- `PUT/PATCH /api/faqs/<id>/`
- Requires authentication
- Translations are updated automatically

## Admin Interface

Access the admin interface at `/admin/` to manage FAQs:
- Create/Edit/Delete FAQs
- View and modify translations
- Toggle FAQ visibility
- Track creation and update timestamps

### Admin Features
- Rich text editing for answers
- Collapsible translation sections
- Search and filter capabilities
- List display with truncated questions

## Caching

The system uses Redis for caching:
- FAQ lists are cached for 1 hour
- Individual translations are cached for 24 hours
- Cache is automatically invalidated on updates

## Translation

Translations are handled automatically using Google Translate:
- New FAQs are translated upon creation
- Empty translations are filled automatically
- Manual translation override is available in admin

## Configuration

### CKEditor Settings
```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
    },
}
```

### REST Framework Settings
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

## Error Handling

The system includes handling for:
- Translation service failures
- Cache connection issues
- Invalid language codes
- Missing content

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
Follow PEP 8 guidelines for Python code.

## Production Deployment

For production:
1. Set `DEBUG=False` in `.env`
2. Configure proper `ALLOWED_HOSTS`
3. Use a production-grade database (e.g., PostgreSQL)
4. Set up proper Redis security
5. Configure proper static files serving
6. Use HTTPS
7. Set up proper logging

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Framework
- Django REST Framework
- Google Translate API
- Redis
- CKEditor

## Support

For support, please open an issue in the repository or contact the maintainers.
