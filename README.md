# To Run

1. `docker-compose up --build -d`
2. `docker-compose exec app python manage.py migrate`
3. `docker-compose exec app python manage.py createsuperuser --username="???"`
4. Visit `localhost:8000`
