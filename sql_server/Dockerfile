FROM mcr.microsoft.com/mssql/server:2022-latest

ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=abcDEF123#
ENV MSSQL_PID=Developer
ENV MSSQL_TCP_PORT=1433

WORKDIR /src

COPY filldata.sql ./filldata.sql

EXPOSE 1433

RUN (/opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" &&  /opt/mssql-tools/bin/sqlcmd -S 127.0.0.1 -U SA -P abcDEF123# -i filldata.sql
# CMD (/opt/mssql/bin/sqlservr --accept-eula &) && sleep 10 && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P abcDEF123# -i /src/filldata.sql

# Utilisation de l'image officielle de Microsoft SQL Server 2022
# FROM mcr.microsoft.com/mssql/server:2022-latest

# # Variables d'environnement pour la configuration de SQL Server
# ENV ACCEPT_EULA=Y
# ENV MSSQL_SA_PASSWORD=abcDEF123#
# ENV MSSQL_PID=Developer
# ENV MSSQL_TCP_PORT=1433

# # Copier le script SQL de configuration dans le conteneur
# COPY ./init.sql /docker-entrypoint-initdb.d/

# # Exposer le port sur lequel SQL Server s'exécute
# EXPOSE 1433
