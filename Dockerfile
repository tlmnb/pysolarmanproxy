FROM python:3.9.21-alpine

LABEL org.opencontainers.image.description "pysolarmanproxy is a Python-based proxy server for Solarman devices. It makes the solarman protocol available as normal rtu-over-tcp modbus."

ARG PYSOLARMAN_VERSION

RUN apk add git

RUN pip install git+https://github.com/tlmnb/pysolarmanproxy@${PYSOLARMAN_VERSION}

ENTRYPOINT ["pysolarmanproxy"]
