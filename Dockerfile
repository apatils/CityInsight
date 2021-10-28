FROM python:3.6-slim
LABEL author="patilakashsuresh@gmail.com"

COPY web_app.py .
COPY requirements.txt .
COPY templates /templates

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "web_app.py"]