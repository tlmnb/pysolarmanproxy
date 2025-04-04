FROM python:3.9.21-alpine

ARG PYSOLARMAN_VERSION

RUN apk add git

RUN pip install git+https://github.com/tlmnb/pysolarmanproxy@${PYSOLARMAN_VERSION}

ENTRYPOINT ["pysolarmanproxy"]
