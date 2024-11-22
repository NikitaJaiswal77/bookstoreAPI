## Features

- Create a new book
- Retrieve a list of all books or a specific book by ID
- Update book details (title, author, publication date, ISBN, and price)
- Delete a book
- Authentication using JWT
- Pagination for the list of books
- Filtering by title, author, ISBN, and price

## Endpoints

- **POST /api/register/**: Register a new user
- **POST /api/token/**: Obtain JWT token
- **GET /api/books/**: List all books (with pagination)
- **POST /api/books/**: Add a new book
- **GET /api/books/{id}/**: Retrieve a specific book by ID
- **PUT/PATCH /api/books/{id}/**: Update book details
- **DELETE /api/books/{id}/**: Delete a specific book

## Authentication

This API uses JWT (JSON Web Token) authentication. To access the endpoints, you need to first register a user, then obtain a token by using the `/api/token/` endpoint.

## requirements.txt
pip install -r requirements.txt

## Apply the migrations
python manage.py migrate
