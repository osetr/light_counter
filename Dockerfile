FROM python:3

COPY ./project /project

WORKDIR project

RUN /bin/bash -c "pip3 install -r requirements.txt;"

RUN /bin/bash -c "chmod +x ./entrypoint.sh"