FROM python:3.11.1-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]