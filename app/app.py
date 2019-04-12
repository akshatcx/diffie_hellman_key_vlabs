from flask import Flask
from .controller import main
#from .models import db

app = Flask(__name__)
app.register_blueprint(main)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
