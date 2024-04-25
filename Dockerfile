FROM ubuntu:22.04

RUN apt-get -y update

RUN apt install -y python3 && apt install -y python3-pip 

RUN apt-get install -y sqlite3 libsqlite3-dev

COPY run.py ./run.py

COPY requirements.txt ./requirements.txt

COPY Event ./Event

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "run", "--host=0.0.0.0"]