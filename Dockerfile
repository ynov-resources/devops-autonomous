FROM python:3.9-slim
COPY requirements.txt /app/requirements.txt
COPY src/ /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]