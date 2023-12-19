migrate:
	docker compose exec -it api python manage.py migrate 

migrations:
	docker compose exec -it api python manage.py makemigrations

setup: start migrate

start:
	docker compose up -d --remove-orphans

stop:
	docker compose down

clean: stop
	docker image rm api_image

tests:
	docker compose exec -it api python manage.py test chat.tests -v 2

update_requirements: clean setup

coverage:
	docker compose exec -it api coverage run manage.py test chat.tests && coverage report