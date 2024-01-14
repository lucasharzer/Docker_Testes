FROM python:3.10-slim

WORKDIR /app

# Instalação do curl e wget
RUN apt-get update && apt-get install -yqq curl wget

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade selenium webdriver_manager

RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get install -yqq firefox-esr

COPY . /app

# Run app.py when the container launches
CMD ["python", "main.py"]