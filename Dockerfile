FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir requests==2.31.0 python-multipart==0.0.9 python-dotenv==1.0.1 fastapi==0.110.3 uvicorn==0.29.0 starlette==0.37.2
COPY . .
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]