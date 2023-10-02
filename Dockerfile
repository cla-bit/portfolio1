FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/

RUN apt-get update
RUN apt-get install -y cron
RUN python3 -m pip install pip --upgrade

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# django-crontab logs
RUN mkdir /cron
RUN touch /cron/cron.log

EXPOSE 8000

CMD ["sh", "-c", "python manage.py crontab add && service cron start && python manage.py runserver 0.0.0.0:8000 && tail -f /cron/cron.log"]
