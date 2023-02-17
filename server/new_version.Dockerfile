FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip
RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /bin/cloud_sql_proxy
RUN chmod +x /bin/cloud_sql_proxy
RUN mkdir /cloudsql; chmod 777 /cloudsql

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

#CMD [ "gunicorn", "-b", "0.0.0.0:80", "main:app"]

