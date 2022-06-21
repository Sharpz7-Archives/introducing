from flask import Flask, jsonify, request
from introducing import faces

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 50000 }
]


@app.route('/')
def get_incomes():
    """
    Returns all incomes
    """

    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    """
    Adds a new income
    """

    incomes.append(request.get_json())
    return '', 204


@app.route('/face')
def get_face():
    """
    Returns a fake face
    """

    return faces.get_fake_face()