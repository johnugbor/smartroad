# Dockerfile
FROM python:3.10-slim

# Prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# 1. Install system dependencies for GeoDjango (GDAL, PROJ, GEOS)
# 'netcat-openbsd' is used to wait for the DB to be ready
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 3. Copy project
COPY . /app/

# 4. Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]