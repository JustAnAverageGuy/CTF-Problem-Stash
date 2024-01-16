FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh impossible
WORKDIR /home/impossible

COPY ./chall.py ./
COPY ./flag.txt /

RUN chown -R root:impossible /home/impossible && \
     chmod 750 /home/impossible && \
     chmod 550 /home/impossible/chall.py && \
     chown root:impossible /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31337

CMD ["socat", "-T60", "TCP-LISTEN:31337,reuseaddr,fork,su=impossible","EXEC:/home/impossible/chall.py"]
