FROM python:3.8-slim-buster

WORKDIR /app

COPY ./ /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
