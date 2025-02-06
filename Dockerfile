FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install requests flask
EXPOSE 8000
ENTRYPOINT ["python", "app.py"]