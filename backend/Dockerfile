FROM python:3.11-slim

WORKDIR /app

# Copy the root-level requirements.txt to /app
COPY ../requirements.txt /app/requirements.txt

# Copy the entire backend folder to /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.config.settings

CMD ["gunicorn", "backend.config.wsgi:application", "--bind", "0.0.0.0:8000"]
