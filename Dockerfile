FROM python:3.9-slim-buster

ENV TZ="Asia/Jakarta"
ENV GIT_PYTHON_REFRESH=quiet

RUN apt update
RUN apt -y install git

RUN git clone https://github.com/ilhamsrc/fsub /app
RUN chmod 777 /app

RUN git config --global user.name "fsub"
RUN git config --global user.email "fsub@e.mail"

WORKDIR /app

RUN pip3 install -r req*txt

CMD ["bash", "./start"]