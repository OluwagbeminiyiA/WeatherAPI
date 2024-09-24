
---

# WeatherAPI 🌦️

WeatherAPI is a simple yet powerful RESTful API built with Django Rest Framework that allows users to fetch real-time weather information based on location. The API is designed to efficiently handle weather data requests and caches responses to improve performance. Perfect for apps needing current weather data without overwhelming the weather service with repeated calls.

## Features ✨

- 🌍 **Real-Time Weather Data**: Fetch real-time weather information based on the user's location.
- 🚀 **Caching with Redis**: Responses are cached for 2 hours using Redis to reduce unnecessary calls to the weather API and improve response times.
- 🛠️ **Django Rest Framework**: Utilizes the Django Rest Framework for a clean, well-structured API implementation.
- ⚡ **Efficient API**: Query parameters are validated, and the API handles invalid requests gracefully.
- 🔒 **Configurable Caching**: Customizable cache duration and easy integration with Redis.

---

## Table of Contents 📖

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Caching](#caching)
5. [Environment Variables](#environment-variables)
6. [License](#license)

---

## Installation 💻

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/OluwagbeminiyiA/WeatherAPI.git
cd WeatherAPI
```

### 2. Set up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# On Windows:
# .venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set up Redis (for caching)
Make sure Redis is installed and running. You can start Redis with:

```bash
redis-server --port 6380
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Your local instance of WeatherAPI should now be running at `http://127.0.0.1:8000`.

---

## Usage 🚀

### Fetch Weather Data
You can fetch weather data by sending a GET request to the API with a location query parameter.

Example:

```bash
curl -X GET "http://127.0.0.1:8000/?location=lagos" -H "accept: application/json"
```

---

## API Endpoints 🔗

### 1. **Get Weather Data** (GET `/`)
Fetches real-time weather data based on the location provided in the query parameters.

- **URL**: `/`
- **Method**: `GET`
- **Query Parameters**: 
  - `location`: (string) Location to fetch weather data for.

#### Example Request:
```bash
GET /?location=lagos
```

#### Example Response:
```json
{
    "date": "2024-09-24",
    "conditions": "Clear",
    "description": "Clear conditions throughout the day.",
    "temperature": "79.7 °F",
    "humidity": 49.8,
    "snow": 0.0
}
```

---

## Caching 🧠

To improve performance, the WeatherAPI uses Redis for caching. When a user requests weather data for a location, the response is cached for **2 hours**. This prevents unnecessary repeated calls to the weather service for the same location, reducing latency and improving the user experience.

### Cache Configuration
In the `settings.py` file, the cache is configured using Redis:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6380/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### How to Check if Caching Works
- Send the same request multiple times. The first time, the data is fetched from the weather service, and subsequent requests (within 2 hours) should return faster responses from the cache.
- You can inspect Redis keys by running `redis-cli` and then using `KEYS *` to check for cached data.

---

## Environment Variables ⚙️

The following environment variables should be configured in your project:

- **REDIS_URL**: URL to your Redis instance (e.g., `redis://127.0.0.1:6380/1`).
- **WEATHER_API_KEY**: Your weather service API key (e.g., Visual Crossing (Recommended), OpenWeatherMap, WeatherAPI).

You can use a `.env` file to store these variables securely:

```
REDIS_URL=redis://127.0.0.1:6380/1
WEATHER_API_KEY=your_weather_api_key_here
```

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributions 👥

Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

---

## Acknowledgments 🙌

- [Django Rest Framework](https://www.django-rest-framework.org/) for making API development easy.
- [Redis](https://redis.io/) for efficient caching.

---

## Contact ✉️

Feel free to reach out for any questions or feedback:

- **GitHub**: [OluwagbeminiyiA](https://github.com/OluwagbeminiyiA)
- **LinkedIn**: [Gbeminiyi Agbedejobi](https://www.linkedin.com/in/gbeminiyi-agbedejobi)

---
