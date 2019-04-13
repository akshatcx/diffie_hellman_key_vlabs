from flask import Flask
from .controller import main
from flask_sqlalchemy import SQLAlchemy
# from .models import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.register_blueprint(main)
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
