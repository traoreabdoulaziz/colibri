# Use the official lightweight Python image.
FROM python:3.8-slim

# Copy local code to the container image.
#ENV /app /app
WORKDIR /app
COPY ./requirements.txt /app
COPY ./secrets.json /app
COPY ./secrets.json.gpg /app
COPY ./gcloud-service-key.json /app
# Install production dependencies.
RUN pip install -r requirements.txt
COPY . /app
ARG ENV
ENV WORK=$ENV
ENV GOOGLE_APPLICATION_CREDENTIALS=gcloud-service-key.json
RUN echo ${WORK}
RUN echo ${GOOGLE_APPLICATION_CREDENTIALS}
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  src.main:app 