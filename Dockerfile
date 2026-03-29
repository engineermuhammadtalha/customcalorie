FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn python-multipart requests python-dotenv
COPY . .
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]