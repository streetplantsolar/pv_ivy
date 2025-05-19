FROM python:3.11-slim

# Set the working directory to the backend folder
WORKDIR /backend

# Copy only the requirements.txt file
COPY ../requirements.txt /backend/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire backend folder
COPY . /backend

# Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Start the application using Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
