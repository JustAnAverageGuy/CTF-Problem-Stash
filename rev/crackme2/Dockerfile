FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh crackme2
WORKDIR /home/crackme2

COPY ./crackme2 ./
COPY ./flag.txt /

RUN chown -R root:crackme2 /home/crackme2 && \
     chmod 750 /home/crackme2 && \
     chmod 550 /home/crackme2/crackme2 && \
     chown root:crackme2 /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 61337

CMD ["socat", "-T60", "TCP-LISTEN:61137,reuseaddr,fork,su=crackme2","EXEC:/home/crackme2/crackme2"]
