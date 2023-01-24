FROM python:3.6

# System prerequisites
RUN apt-get update \
 && apt-get -y install build-essential libpq-dev git \
 && rm -rf /var/lib/apt/lists/*

RUN pip install waitress

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8000

CMD ["waitress-serve", "--host", "0.0.0.0", "app:app"]