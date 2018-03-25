FROM python:3
MAINTAINER Vikas srivastava <er.vikassri@gmail.com>

### Login as a root ###
USER root


### Updating the system ###
RUN apt-get update -y && apt-get upgrade -y

ENV HOME /root


# === Some Environment Variables
ENV    DEBIAN_FRONTEND noninteractive

# === MySQL Installation
RUN apt-get update
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

### Installing needed requiremets ###
ENV requirements="build-essential python-dev python-setuptools python3-pip mysql-server mysql-client libmysqld-dev vim"  

RUN apt-get install $requirements -y && rm -rf /var/lib/apt/lists/*


### Installing pip packages ###
ENV prequirements="pymysql requests numpy pandas"
RUN pip install $prequirements

# creating required folder and adding files 
RUN mkdir -p /home/scripts
RUN chmod 755 /home/scripts
ADD weather /home/scripts
RUN mkdir /home/data

# mysql configuration
ADD build/my.cnf    /etc/mysql/my.cnf

RUN mkdir -p       /etc/service/mysql
ADD build/mysql.sh  /etc/service/mysql/run
ADD build/run.sh /home/scripts/
RUN chmod +x        /etc/service/mysql/run

RUN mkdir -p        /var/lib/mysql/
RUN chmod -R 755    /var/lib/mysql/

ADD build/setup.sh  /etc/mysql/mysql_setup.sh
RUN chmod +x        /etc/mysql/mysql_setup.sh

RUN bash /etc/mysql/mysql_setup.sh

EXPOSE 3306
