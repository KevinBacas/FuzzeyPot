FROM python:2.7

RUN mkdir /code
WORKDIR /code
ADD ./FuzzeyPot/requirements.txt /code/
ADD ./FuzzeyPot/manage.py /code/manage.py
RUN pip install -r requirements.txt
ADD ./FuzzeyPot/FuzzeyPot/ /code/FuzzeyPot/
ADD ./FuzzeyPot/Blog/ /code/Blog/
RUN python manage.py migrate

EXPOSE 5000
CMD python manage.py runserver 0.0.0.0:5000
