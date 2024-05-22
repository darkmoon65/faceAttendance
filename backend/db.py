from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
load_dotenv()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'Test'

mysql = MySQL(app)