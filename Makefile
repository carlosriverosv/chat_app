migrate:
	docker compose exec -it api python manage.py migrate 

migrations:
	docker compose exec -it api python manage.py makemigrations

setup: start migrate

start:
	docker compose up -d --remove-orphans

stop:
	docker compose down

clean:
	docker compose down
	docker image rm api_image

tests:
	docker compose exec -it api python manage.py test chat.tests
