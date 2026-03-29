FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir requests==2.31.0 python-multipart==0.0.9 python-dotenv==1.0.1

COPY . .

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]