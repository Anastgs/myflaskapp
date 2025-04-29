# Stage 1: Install dependencies
FROM python:3.10-slim AS builder
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --target=/app/install --no-cache-dir -r requirements.txt
 
# Stage 2: Final image
FROM python:3.10-slim
 
WORKDIR /app
 
COPY --from=builder /app/install /usr/local/lib/python3.10/site-packages
COPY app.py .
COPY data ./data
 
EXPOSE 5000
 
CMD ["python", "app.py"]