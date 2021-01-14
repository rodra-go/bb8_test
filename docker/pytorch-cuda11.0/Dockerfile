FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime
LABEL MAINTAINER="Rodrigo Cunha <rodrigo.cunha@usp.br>"


RUN apt-get update && \
apt-get upgrade -y
RUN apt-get install bash

ENV GROUP_ID=1000 \
    USER_ID=1000 \
    USER=bb8_test \
    PASS=pass

RUN addgroup --gid $GROUP_ID $USER
RUN adduser --uid $USER_ID --ingroup $USER --shell /bin/bash --disabled-password --gecos "" $USER
RUN usermod -aG 100 $USER
RUN usermod -aG sudo $USER
RUN echo "$USER:$PASS" | chpasswd

ADD requirements.txt /var/$USER/
ADD setup.py /var/$USER/
RUN pip install --upgrade pip setuptools
RUN pip install -r /var/$USER/requirements.txt
RUN python /var/$USER/setup.py

USER $USER
WORKDIR /home/$USER/code/
