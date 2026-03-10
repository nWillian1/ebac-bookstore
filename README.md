# ebac-bookstore
Book store APP from Backend Python course from EBAC

## Prerequisites
Python 3.13
Poetry
Docker && docker-compose

## Quickstart
1º Clone this project
git clone git@github.com:nWillian1/ebac-bookstore.git

2º Instale as dependências
cd bookstore
poetry install

3º Run local dev server:
poetry run manage.py migrate
poetry run python manage.py runserver

4º Run docker dev server environment:
docker-compose up -d --build 
docker-compose exec web python manage.py migrate

5º Run tests inside of docker:
docker-compose exec web python manage.py test

