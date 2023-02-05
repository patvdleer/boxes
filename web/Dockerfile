FROM python:3.10-bullseye AS builder
# g++ make geos-dev for shapely
# RUN apk update && apk add git g++ make geos-dev
RUN set -eux; \
    apt update; \
    apt install -y --no-install-recommends python3-shapely python3-numpy
WORKDIR /tmp
COPY requirements.txt /tmp
RUN pip3 install -r requirements.txt

ADD https://raw.githubusercontent.com/florianfesti/boxes/master/requirements.txt requirements-boxes.txt
RUN pip3 install -r requirements-boxes.txt

# little dirty hack to get the current master with this flask branch/version
WORKDIR /app
RUN git clone --depth 1 -b master https://github.com/florianfesti/boxes.git
WORKDIR /app/boxes/web
COPY . /app/boxes/web

EXPOSE 8001
ENTRYPOINT ["python3"]
CMD ["serve.py"]
