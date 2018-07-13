from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# python3 必须加pymysql 不然会有问题
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:vanke@localhost:9999/flask_db?charset=utf8'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)