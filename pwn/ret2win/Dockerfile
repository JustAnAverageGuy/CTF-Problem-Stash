FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat gcc-multilib

RUN useradd -ms /bin/sh ret2win
WORKDIR /home/ret2win

COPY ./ret2win ./
COPY ./flag.txt /
COPY ./fake_flag.txt /

RUN chown -R root:ret2win /home/ret2win && \
     chmod 750 /home/ret2win && \
     chmod 550 /home/ret2win/ret2win && \
     chown root:ret2win /flag.txt && \
     chmod 440 /flag.txt && \
     chown root:ret2win /fake_flag.txt && \
     chmod 440 /fake_flag.txt


EXPOSE 31141

CMD ["socat", "-T60", "TCP-LISTEN:31141,reuseaddr,fork,su=ret2win","EXEC:/home/ret2win/ret2win"]
