FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
ruby \
ruby-dev \
build-essential \
libxml2-dev \
libxslt-1dev \
zlib 1 g-dev \
libsqlite3-dev \
nodejs

RUN gem install rails

RUN mkdir -p /src && cd /src && rails new my-app
WORKDIR /src/my-app

CMD ["rails", "server", "--binding", "0.0.0.0", "--port", "3000"]
EXPOSE 3000
