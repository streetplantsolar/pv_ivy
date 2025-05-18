FROM python:3.11-slim

WORKDIR /app

COPY ./backend /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
