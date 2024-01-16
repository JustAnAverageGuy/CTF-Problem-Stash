FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat python3

RUN useradd -ms /bin/sh math_game
WORKDIR /home/math_game

COPY ./math_game.py ./
COPY ./flag.txt /

RUN chown -R root:math_game /home/math_game && \
     chmod 750 /home/math_game && \
     chmod 550 /home/math_game/math_game.py && \
     chown root:math_game /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 31139

CMD ["socat", "-T60", "TCP-LISTEN:31139,reuseaddr,fork,su=math_game","EXEC:/home/math_game/math_game.py"]
