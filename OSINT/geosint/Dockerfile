FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3 python3-pip

RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/ctf

COPY . .

RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/server.py
RUN chmod 440 /home/ctf/templates/*

RUN python3 -m pip install -r flask
USER ctf
CMD ["python3", "/home/ctf/server.py"]
