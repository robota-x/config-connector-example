FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY processor.py /app/

ENTRYPOINT ["python"]
CMD ["processor.py"]