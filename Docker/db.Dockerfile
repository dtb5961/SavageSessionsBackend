FROM postgres:9.6.20
COPY *.sql /docker-entrypoint-initdb.d/