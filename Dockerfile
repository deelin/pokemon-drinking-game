FROM python:latest

WORKDIR /home/pokemon/

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./pokemon ./

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
