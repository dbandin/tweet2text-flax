from python:3.6

RUN mkdir -p /opt/dbandin/tweet2text
WORKDIR /opt/dbandin/tweet2text

RUN pip3 install --upgrade pip
COPY requirements*.txt ./
RUN pip3 install -r requirements.txt

COPY . ./

LABEL maintainer="Diego Leonardo Bandin <dbandin@gmail.com>"
LABEL source="https://github.com/dbandin/tweet2text-flax/tree/web-version"
ARG commit
LABEL commit="$commit"

ENV PORT 5000
ENV FLASK_APP tweet2text/app.py

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["flask", "run", "--host=0.0.0.0"]