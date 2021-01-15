# SavageSessionsBackend
Backend Application to talk to Database for Savage Sessions

## Database Considerations
NoSQL seems to be the most advantageous option due to prior experience and the uncertainty that the application will undergo.
A SQL database can be explored once the application is more mature.

Postgres since I have prior experience is the NoSQL instance chosen



## Helpful Links/ Tips

docker exec -it <ContainerName> /bin/bash
https://hub.docker.com/_/postgres

### Fatal Root Does Not Exist Error
https://stackoverflow.com/questions/60193781/postgres-with-docker-compose-gives-fatal-role-root-does-not-exist-error

psql -U tester -d SavageSessions

Command to see what is using a port
sudo netstat -nlp | grep 8080

Use kill to terminate