FROM python:3.10-slim
EXPOSE 5000/http 
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
CMD ["python3", "hello_api.py"]
