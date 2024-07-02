FROM python:3.11

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

CMD ["gunicorn", "bike_rental.wsgi:application", "--bind", "0.0.0.0:8000"]
