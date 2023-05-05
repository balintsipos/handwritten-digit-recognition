FROM python:3.8-slim-buster

WORKDIR /app

COPY static /app/static
COPY templates /app/templates
COPY app.py /app
COPY requirements.txt /app
COPY typeface_model_best.pkl /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/app/app.py"]