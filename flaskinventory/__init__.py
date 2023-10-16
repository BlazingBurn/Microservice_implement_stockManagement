from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'

# Configuration de la base de données Azure SQL
server = "tcp:stockmanagementserve.database.windows.net,1433"
database = "StockManagement"
username = "azureuser"
password = "Qsdfghjklm12"

driver = '{ODBC Driver 18 for SQL Server}'

# Chaîne de connexion ODBC
odbc_str = 'Driver='+driver+';Server='+server+';Database='+ database + ';Uid=' + username  + ';Pwd='+ password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)

# Configuration de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = connect_str

db = SQLAlchemy(app)

from flaskinventory import routes

#db.create_all()
#db.session.commit()
