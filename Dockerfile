FROM python:3.9-slim
RUN pip install --no-cache-dir flask
COPY app.py /app.py
EXPOSE 8080
CMD ["python", "/app.py"]