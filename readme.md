# Qarbon 🌍

*School project — HE-Arc Neuchâtel*

Qarbon is a web app for discovering local events and places, built as part of a course at HE-Arc. [One-line description of the actual purpose/target audience — e.g. "helps users find eco-friendly events and places near them" — please confirm/adjust.]

## ✨ Features

- 📍 Browse places (`places.json`) [describe: categories? map view? search?]
- 📅 Browse and/or manage events (`events.json`) [describe: filtering by date/category?]
- 🎨 UX mockups designed before development (see [`mockups/`](./mockups))
- 🔐 [Authentication if any — register/login via dj-rest-auth?]
- [Any other feature: favorites, ratings, admin panel...]

## 🛠️ Tech stack

| Layer | Technology |
|---|---|
| Frontend | Vue 3 + Vite |
| Backend | Django + Django REST Framework |
| Database | SQLite |
| Auth | JWT (dj-rest-auth) [confirm if actually used] |

This project was bootstrapped from a Django/Vue starter template provided by HE-Arc, then built out with the features above.

## 🚀 Getting started

### Prerequisites
- Node.js
- Python 3

### Backend

```bash
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
npm install
npm run dev
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/

## 📸 Screenshots / mockups

See the [`mockups/`](./mockups) folder for the initial UX design work.

[Add 1-2 screenshots of the running app here if available]

## 👨‍💻 Author

**Omar Griggio** — [github.com/OmarGriggio](https://github.com/OmarGriggio)

School project built at HE-Arc Neuchâtel as part of the Business IT (Informatique de gestion) program.
