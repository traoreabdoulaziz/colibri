# Use the official lightweight Python image.
FROM python:3.7-slim

# Copy local code to the container image.
#ENV /app /app
WORKDIR /app
COPY ./requirements.txt /app
COPY ./secrets.json.gpg /app
COPY ./secrets.json.gpg /app
# Install production dependencies.
RUN pip install -r requirements.txt

COPY . /app

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  app.main:app 