# Qarbon 🌍

*School project — HE-Arc Neuchâtel*

Qarbon is a web app for discovering local events and places, built as part of a course at HE-Arc. It helps users discover local places and events, rate and comment on places, and register for events.

## ✨ Features

- 📍 Browse and search places (`places.json`) by name, street or locality — with photo, average rating and comments
- 📅 Browse, search and register for events (`events.json`) — filter by event name, place, organizer, or registration status; capacity limit with automatic waitlist
- 🎨 UX mockups designed before development (see [`mockups/`](./mockups))
- 🔐 Authentication via dj-rest-auth + JWT (register/login/logout, token refresh)
- ⭐ Ratings (0-5) & comments on places, 💬 direct messaging between users (inbox), 📧 email notifications to event participants, 🖼️ profile with bio/location

## 🛠️ Tech stack

| Layer | Technology |
|---|---|
| Frontend | Vue 3 + Vite |
| Backend | Django + Django REST Framework |
| Database | SQLite |
| Auth | JWT (dj-rest-auth) |

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
