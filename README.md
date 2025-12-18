# URL Shortener API

A simple URL shortener backend built using Flask and SQLite.

## Features
- Create short URLs
- Redirect to original URLs
- URL validation
- Proper HTTP status codes
- Persistent storage using SQLite

## Tech Stack
- Python
- Flask
- SQLite

## API Endpoints

### POST /shorten
Creates a short URL.

**Request**
```json
{
  "url": "https://www.example.com"
}
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
