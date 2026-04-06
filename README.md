# PrEng Lab 3 — Users REST API

Simple REST API for user management built with Flask.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Server runs at `http://localhost:5000`.

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get user by ID |
| POST | `/users` | Create user |
| PUT | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |
| GET | `/users/search?name=<query>` | Search users by name |
| GET | `/users/stats` | Get user statistics |

## Request / Response

**POST /users** — create a user:
```json
{ "name": "Alice", "age": 25 }
```

**GET /users/stats** — statistics:
```json
{
  "total": 2,
  "avg_age": 27.5,
  "min_age": 25,
  "max_age": 30
}
```

**Validation rules:**
- `name` — required, string
- `age` — required, integer, 0–150

## Team

| Name | GitHub |
|------|--------|
| Алёшкин Александр Андреевич | [@Axlifreeway](https://github.com/Axlifreeway) |
| Бекевич Иван Михайлович | [@Impohimoza](https://github.com/Impohimoza) |
| Березин Роман Вячеславович | [@Shankly8642](https://github.com/Shankly8642) |
| Вологин Никита Сергеевич | [@malakia3491](https://github.com/malakia3491) |
