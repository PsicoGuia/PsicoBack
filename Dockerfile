# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0


# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get install -yf build-essential sysv-rc-conf gcc git python python-dev python3 python3-dev  && \
  apt-get install -yf python-setuptools python-setuptools python-pip python3-setuptools python3-pip binutils libproj-dev gdal-bin postgresql-server-dev-9.3 libjpeg8-dev && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir -p /srv/www/app & mkdir -p /srv/www/bin & mkdir -p /srv/www/static
ADD PsicoBack /srv/www/app
RUN pip3 install -r /srv/www/app/requriments.txt
ADD deployenv/bin/ /srv/www/bin/
RUN chmod +x /srv/www/bin/*

EXPOSE 8000
ENTRYPOINT ["/srv/www/bin/gunicorn.sh"]
