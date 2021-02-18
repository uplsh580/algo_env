FROM python:3.6.10

WORKDIR /app
RUN apt-get update && apt-get upgrade g++ build-essential git net-tools vim openssh-server make -y
COPY requirement.txt .
RUN pip install -r requirement.txt
RUN rm requirement.txt
EXPOSE 22

CMD ["/bin/bash"]