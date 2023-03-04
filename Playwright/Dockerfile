FROM python:3

COPY . .

RUN pip install -r requirements.txt

RUN playwright install

RUN playwright install-deps

WORKDIR /app

CMD ["python", "/app/main.py"]