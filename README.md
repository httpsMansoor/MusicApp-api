# Music API

A Django REST Framework API for managing songs and singers with authentication and advanced search capabilities.

## Features

- 🔐 Token-based authentication
- 🎵 Song management (CRUD operations)
- 🎤 Singer management with user accounts
- 🔍 Advanced search capabilities
  - Case-insensitive partial matching
  - Search by title and singer name
- 👤 User-specific song access
- 🔒 Custom permissions for song management

## Prerequisites

- Python 3.8+
- Django 5.2+
- Django REST Framework
- django-filter

## Installation

1. Clone the repository:
```bash
git clone https://github.com/httpsMansoor/MusicApp-api.git
cd MusicApp-api
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api-token-auth/` - Get authentication token

### Songs
- `GET /songs/` - List all songs
- `POST /songs/` - Create a new song
- `GET /songs/{id}/` - Retrieve a specific song
- `PUT /songs/{id}/` - Update a song
- `DELETE /songs/{id}/` - Delete a song

### Singers
- `GET /singers/` - List all singers
- `POST /singers/` - Register a new singer
- `GET /singers/{id}/` - Retrieve a specific singer
- `PUT /singers/{id}/` - Update a singer
- `DELETE /singers/{id}/` - Delete a singer

## Search and Filtering

### Search
- Use `?search=query` to search songs by title or singer name
- Example: `/songs/?search=bilal`

### Filtering
- Filter by singer name: `/songs/?singer__name=bilal`
- Case-insensitive partial matching is supported

## Authentication

1. Register a singer:
```bash
POST /singers/
{
    "name": "Bilal Saeed",
    "gender": "Male",
    "username": "bilal",
    "password": "your_password"
}
```

2. Get authentication token:
```bash
POST /api-token-auth/
{
    "username": "bilal",
    "password": "your_password"
}
```

3. Use the token in subsequent requests:
```bash
Authorization: Token your_token_here
```

## Rate Limiting

The API implements rate limiting to prevent abuse:
- Anonymous users: 100 requests per day
- Authenticated users: 1000 requests per day

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter)

Project Link: [https://github.com/httpsMansoor/MusicApp-api](https://github.com/httpsMansoor/MusicApp-api) 