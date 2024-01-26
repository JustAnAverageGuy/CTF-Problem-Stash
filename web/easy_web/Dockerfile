FROM ubuntu:latest

RUN apt-get update && apt-get -y install xinetd
RUN apt-get -y install python3 python3-pip curl

RUN groupadd -r ctf && useradd -r -g ctf ctf

COPY templates/ /home/ctf/templates/
COPY requirements.txt /home/ctf/requirements.txt
COPY server.py /home/ctf/server.py

RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/server.py
RUN chmod 440 /home/ctf/requirements.txt
RUN chmod 440 /home/ctf/templates/*

RUN python3 -m pip install -r /home/ctf/requirements.txt

USER ctf
CMD ["python3", "/home/ctf/server.py"]
