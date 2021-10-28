FROM python:3.8-slim-buster

WORKDIR /app

COPY ./ /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD [ "streamlit", "run", "front_app.py", "--server.runOnSave", "TRUE"]
