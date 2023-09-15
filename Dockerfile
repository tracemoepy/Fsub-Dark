# SET BASE IMAGE OS
FROM python:3.9-alpine

# UPDATE AND INSTALL GIT
RUN apk update
RUN apk add --no-cache git

# CLONE REPOSITORY
RUN git clone \
    https://github.com/tracemoepy/Fsub-Dark \
    /home/fsub ; chmod 777 /home/fsub

# WORKDIR
WORKDIR /home/fsub

# SET GIT CONFIG
RUN git config --global user.name "fsub"
RUN git config --global user.email "fsub@e.mail"

# IGNORE PIP WARNING 
ENV PIP_ROOT_USER_ACTION=ignore

# UPDATE PIP
RUN pip install -U pip

# INSTALL REQUIREMENTS
RUN pip install -U \
                --no-cache-dir \
                -r requirements.txt

# COMMAND TO RUN
CMD ["python", "main.py"]