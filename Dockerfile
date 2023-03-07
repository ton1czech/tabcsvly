FROM python:3.10.9

WORKDIR /app

COPY src .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "tabcsvly.py"]