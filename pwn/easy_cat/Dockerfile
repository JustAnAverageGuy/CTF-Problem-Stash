FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat python3

RUN useradd -ms /bin/sh easy_cat
WORKDIR /home/easy_cat

COPY ./easy_cat.py ./

RUN chown -R root:easy_cat /home/easy_cat && \
     chmod 750 /home/easy_cat && \
     chmod 550 /home/easy_cat/easy_cat.py

EXPOSE 31136

CMD ["socat", "-T60", "TCP-LISTEN:31136,reuseaddr,fork,su=easy_cat","EXEC:/home/easy_cat/easy_cat.py"]
