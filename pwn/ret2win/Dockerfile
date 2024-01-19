FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh bank
WORKDIR /home/bank

COPY ./bank ./
COPY ./flag.txt /

RUN chown -R root:bank /home/bank && \
     chmod 750 /home/bank && \
     chmod 550 /home/bank/bank && \
     chown root:bank /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31137

CMD ["socat", "-T60", "TCP-LISTEN:31137,reuseaddr,fork,su=bank","EXEC:/home/bank/bank"]
