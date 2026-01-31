# 🔗 URL Shortener API

A lightweight and efficient URL shortener backend built with **Flask** and **SQLite**.  
This API converts long URLs into short, shareable links and seamlessly redirects users to the original destination.

---

##  Features

- Generate short URLs from long links  
- Redirect short URLs to the original destination  
- URL format validation  
- Proper HTTP status codes and error handling  
- Persistent storage using SQLite  
- Simple REST API design  

---

## 🛠 Tech Stack

- Python  
- Flask  
- SQLite  

---

##  Getting Started

### Prerequisites
- Python 3.x  
- pip  

### Installation

```bash
git clone https://github.com/your-username/url-shortener-api.git
cd url-shortener-api
pip install -r requirements.txt

```
## Run the Server
```bash
python app.py
```
## The API will run at:
```bash
http://127.0.0.1:5000
```
# API Endpoints
1️⃣ Create a Short URL
POST /shorten
Creates a shortened URL for a given long URL.
Request Body

```json
{
  "url": "https://www.example.com"
}
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
```
#Error Responses: 
- 400 Bad Request – Invalid or missing URL
- 500 Internal Server Error – Server-side error
2️⃣ Redirect to Original URL
GET /<short_code>
Redirects the user to the original URL mapped to the short code.
Example
```bash
GET http://127.0.0.1:5000/abc123
```
- 302 Found – Successful redirection
- 404 Not Found – Short URL does not exist

## Example Workflow
1. User submits a long URL via /shorten
2. API returns a shortened URL
3. Visiting the short URL redirects to the original website
