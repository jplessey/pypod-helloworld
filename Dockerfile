FROM python:3.8-slim-buster
LABEL maintainer="Juan Lessey"

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

CMD ["python", "app.py"]    