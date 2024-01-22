FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat gcc-multilib

RUN useradd -ms /bin/sh executable
WORKDIR /home/executable

COPY ./executable ./
COPY ./flag.txt /

RUN chown -R root:executable /home/executable && \
     chmod 750 /home/executable && \
     chmod 550 /home/executable/executable && \
     chown root:executable /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31144

CMD ["socat", "-T60", "TCP-LISTEN:31144,reuseaddr,fork,su=executable","EXEC:/home/executable/executable"]
