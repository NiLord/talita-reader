FROM --platform=$BUILDPLATFORM python:3.8-slim AS builder

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]