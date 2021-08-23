from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://dev:dev@db:5432/default'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.String(255))

    def __init__(self, message):
        self.message = message


@app.route('/')
def index():
    response = jsonify(Message.query.get(1).message)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    db.create_all()
    db.session.add(Message(message='This is my stored message!'))
    db.session.commit()
    app.run(debug=True, host='0.0.0.0', port=8000)
