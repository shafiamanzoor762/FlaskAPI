from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:<password>@localhost/academicsystem'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/academicsystem'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Joe$123@localhost/FYP_Practice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
