FROM python:3.12

RUN apt-get update && apt-get install \
	-y postgresql postgresql-contrib && apt-get clean && pip install --upgrade pip setuptools wheel

USER postgres

RUN service postgresql start && \
    psql -c "CREATE USER user_admin WITH PASSWORD 'admin2411';" && \
    psql -c "CREATE DATABASE challenge_db;" && \
    psql -c "GRANT ALL PRIVILEGES ON DATABASE challenge_db TO user_admin;"

USER root

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY supervisord.conf .

EXPOSE 8000
EXPOSE 5432

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]