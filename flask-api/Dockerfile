FROM python:3.8.6
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install flask
RUN pip install Flask-SQLAlchemy
RUN pip install mysqlclient
EXPOSE 5000
CMD ["python", "main.py"]
