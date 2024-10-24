FROM python:latest
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY .  .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]
