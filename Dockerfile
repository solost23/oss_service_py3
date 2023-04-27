FROM python:3.9.6

WORKDIR /build
COPY . .
RUN pip install -r requirements.txt
RUN apk add tzdata

CMD ["python", "./cmd/main.py"]
