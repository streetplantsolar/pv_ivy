FROM python:3.11-slim

WORKDIR /backend

# Copy the root-level requirements.txt to the backend folder
COPY ../requirements.txt /backend/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the backend folder content
COPY . /backend

# Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.config.settings

# Run Gunicorn
CMD ["gunicorn", "backend.config.wsgi:application", "--bind", "0.0.0.0:8000"]
