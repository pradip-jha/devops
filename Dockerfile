FROM python:3-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src /app
EXPOSE 5000
WORKDIR app

ENTRYPOINT ["python"]
CMD ["hello.py"]
