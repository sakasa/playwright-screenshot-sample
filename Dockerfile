FROM python:3.11

RUN apt -y update && apt -y upgrade

RUN pip install --upgrade pip
RUN pip install playwright

RUN playwright install
RUN playwright install-deps

WORKDIR /work
ENTRYPOINT [ "python", "./pw.py" ]
