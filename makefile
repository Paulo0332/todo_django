# Django + Docker Makefile

# Build Docker images

build:
	docker compose build

# Start services in the foreground

up:
	docker compose up

# Start services in the background

up-detached:
	docker compose up -d

# Stop and remove containers, networks, volumes

down:
	docker compose down -v

# Rebuild images without cache

rebuild:
	docker compose build --no-cache

# Open bash shell in the DJango container

bash:
	docker compose exec web bash

# Run Django migrations

migrate:
	docker compose exec web python manage.py migrate

# Create a Django superuser

createsuperuser:
	docker compose exec web python manage.py createsuperuser

# Open Django shell

shell:
	docker compose exec web python manage.py shell

# Run tests

test:
	docker compose exec web pytest

# Clean unused Docker resources

clean:
	docker system prune-ag
	docker volume prune -f