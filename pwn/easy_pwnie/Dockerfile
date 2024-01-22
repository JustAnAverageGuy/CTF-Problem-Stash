FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat python3

RUN useradd -ms /bin/sh easy_pwnie
WORKDIR /home/easy_pwnie

COPY ./easy_pwnie.py ./
COPY ./flag.txt /

RUN chown -R root:easy_pwnie /home/easy_pwnie && \
     chmod 750 /home/easy_pwnie && \
     chmod 550 /home/easy_pwnie/easy_pwnie.py && \
     chown root:easy_pwnie /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31142

CMD ["socat", "-T60", "TCP-LISTEN:31142,reuseaddr,fork,su=easy_pwnie","EXEC:/home/easy_pwnie/easy_pwnie.py"]
