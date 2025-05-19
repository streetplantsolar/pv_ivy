FROM python:3.11-slim

# Set working directory to backend
WORKDIR /backend

# Copy the root-level requirements.txt to /backend
COPY ../requirements.txt /backend/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy backend contents to /backend
COPY . /backend

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Start the application using Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
