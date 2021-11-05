FROM python:3.7.12

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app/

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000" ]
