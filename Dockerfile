FROM python:3.12.0a4-slim-bullseye

RUN apt update -y && apt install wget unzip sudo -y
RUN adduser app
RUN echo "app:app" | chpasswd
RUN adduser app sudo

COPY ./.docker/entrypoint.sh /
RUN chmod a+x /entrypoint.sh

RUN cd /home && wget https://github.com/Lucksi/Mr.Holmes/archive/refs/heads/master.zip
RUN cd /home && unzip master.zip
RUN cd /home && mv Mr.Holmes-master/* app
RUN chown -R app:app /home/app 

USER app
WORKDIR /home/app/
RUN echo "desktop" >> ./Display/Display.txt
RUN echo "python3 ./MrHolmes.py" >> ./install.sh
RUN chmod a+x ./install.sh

ENTRYPOINT ["/entrypoint.sh"]