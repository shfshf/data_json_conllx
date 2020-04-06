FROM python:3.6.10

ADD ./docker_test /code
RUN mkdir /app

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY all_in_one.bash /app/all_in_one.bash

CMD ["bash", "/app/all_in_one.bash"]