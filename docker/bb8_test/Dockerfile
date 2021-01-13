FROM nvidia/cuda:11.0-base
LABEL MAINTAINER="Rodrigo Cunha <rodrigo.cunha@usp.br>"

RUN apt-get update && \
apt-get upgrade -y
RUN apt-get install bash
RUN apt-get install python3-pip -y

ENV GROUP_ID=1000 \
    USER_ID=1000 \
    USER=taskq \
    PASS=pass

RUN addgroup --gid $GROUP_ID $USER
RUN adduser --uid $USER_ID --ingroup $USER --shell /bin/bash --disabled-password --gecos "" $USER
RUN usermod -aG 100 $USER
RUN usermod -aG sudo $USER
RUN echo "$USER:$PASS" | chpasswd

ADD requirements.txt /var/$USER/
ADD setup.py /var/$USER/
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /var/$USER/requirements.txt
RUN python3 /var/$USER/setup.py

USER $USER
WORKDIR /home/$USER/
