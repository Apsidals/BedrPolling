FROM python:3.11-slim
WORKDIR /app
COPY poll-service/requirements.txt .
RUN pip install -r requirements.txt
COPY poll-service/app.py .
CMD ["python", "app.py"]