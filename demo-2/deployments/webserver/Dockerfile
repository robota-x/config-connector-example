FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY webserver.py templates /app/

ENV FLASK_APP=webserver.py

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]