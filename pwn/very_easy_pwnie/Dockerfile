FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat python3

RUN useradd -ms /bin/sh very_easy_pwnie
WORKDIR /home/very_easy_pwnie

COPY ./very_easy_pwnie.py ./
COPY ./flag.txt /

RUN chown -R root:very_easy_pwnie /home/very_easy_pwnie && \
     chmod 750 /home/very_easy_pwnie && \
     chmod 550 /home/very_easy_pwnie/very_easy_pwnie.py && \
     chown root:very_easy_pwnie /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31142

CMD ["socat", "-T60", "TCP-LISTEN:31142,reuseaddr,fork,su=very_easy_pwnie","EXEC:/home/very_easy_pwnie/very_easy_pwnie.py"]
