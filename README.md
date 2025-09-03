# 📝 To-Do List (Django + Docker + PostgreSQL)

A simple **To-Do List web application** built with **Django**, running on **PostgreSQL** inside **Docker**.  
This project was designed with **production practices** in mind, including containerization, database health checks, and Git workflow.

---

## ✨ Features
- Create, read, update, and delete tasks (CRUD).
- Mark tasks as completed or uncompleted.
- Sort tasks by:
  - Name
  - Creation date
  - Update date
  - Status (completed/uncompleted)

---

## 🛠️ Tech Stack
- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>
```
### 2. Build and start containers
```bash
docker compose up --build -d
```
### 3. Apply database migrations
```bash
docker compose exec web python manage.py migrate
```
### 4. Create a superuser (for Django admin)
```bash
docker compose exec web python manage.py createsuperuser
```
### 5. Access the app
App: http://localhost:8000/tasks
Admin: http://localhost:8000/admin
