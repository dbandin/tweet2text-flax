FROM python:3.8

WORKDIR /tweet2text

COPY tweet2text ./tweet2text/
COPY requirements ./requirements/
COPY pip_compile.sh setup.py ./

RUN pip install -r requirements/dev.txt
RUN pip install -e .

ENTRYPOINT [ "tweet2text" ]
