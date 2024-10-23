FROM python:latest
WORKDIR /srv
COPY .  .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]
