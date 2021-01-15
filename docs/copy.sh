docker cp ./$1 savagesessionsbackend_db_1:/docker-entrypoint-initdb.d/$1
docker exec -i savagesessionsbackend_db_1 psql -U tester -d SavageSessions -f docker-entrypoint-initdb.d/$1