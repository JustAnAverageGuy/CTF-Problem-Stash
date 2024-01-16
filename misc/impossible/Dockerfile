FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh bank_2
WORKDIR /home/bank_2

COPY ./bank_2 ./
COPY ./flag.txt /

RUN chown -R root:bank_2 /home/bank_2 && \
     chmod 750 /home/bank_2 && \
     chmod 550 /home/bank_2/bank_2 && \
     chown root:bank_2 /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31138

CMD ["socat", "-T60", "TCP-LISTEN:31138,reuseaddr,fork,su=bank_2","EXEC:/home/bank_2/bank_2"]
