FROM python:3.12

RUN apt-get update && apt-get install \
	-y postgresql postgresql-contrib && apt-get clean

RUN service postgresql start && \
    sudo -u postgres psql -c "CREATE USER user_admin WITH PASSWORD '';" && \
    sudo -u postgres psql -c "CREATE DATABASE challenge_db;" && \
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE challenge_db TO user_admin;"

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 5432

CMD service postgresql start && uvicorn api.main:app --host 0.0.0.0 --port 8000