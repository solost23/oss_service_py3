FROM python:3.9.6

WORKDIR /
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "./cmd/main.py"]
