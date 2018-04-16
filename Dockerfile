FROM python:3.6

WORKDIR /opt/bot

COPY ./bot /opt/bot

COPY requirenments.txt /opt/requirenments.txt
RUN [ "pip", "install", "--upgrade", "pip" ]
RUN [ "pip", "install", "-r", "/opt/requirenments.txt" ]

EXPOSE 8443

CMD python bot.py
