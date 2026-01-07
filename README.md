# 🔗 URL Shortener API

A lightweight and efficient URL shortener backend built with **Flask** and **SQLite**.  
This API converts long URLs into short, shareable links and seamlessly redirects users to the original destination.

---

## ✨ Features

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

## 🚀 Getting Started

### Prerequisites
- Python 3.x  
- pip  

### Installation

```bash
git clone https://github.com/your-username/url-shortener-api.git
cd url-shortener-api
pip install -r requirements.txt

```

**Request**
```json
{
  "url": "https://www.example.com"
}
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
