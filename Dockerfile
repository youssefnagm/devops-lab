FROM python:3.12-slim
WORKDIR /app
COPY check_sites.py .
CMD ["python", "check_sites.py"]
