FROM python:latest
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir requests==2.25.1

CMD ["python","meteo.py"]



