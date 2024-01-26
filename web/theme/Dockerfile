FROM python:3.10-slim-buster

RUN pip3 install flask
COPY flag.txt /

WORKDIR /app
COPY app/* /app/
COPY app/templates/* /app/templates/
COPY app/themes/* /app/themes/

EXPOSE 41342

ENTRYPOINT ["python3", "server.py"]
