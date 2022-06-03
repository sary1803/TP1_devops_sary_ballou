FROM python:latest
ADD . /app/
WORKDIR /app
RUN pip install requests

CMD ["python,""meteo.py"]

