import http.client

from flask import Flask, jsonify, abort

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return jsonify(result=CALCULATOR.add(float(op_1), float(op_2)))
    except TypeError as e:
        abort(400, str(e))


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return jsonify(result=CALCULATOR.substract(float(op_1), float(op_2)))
    except TypeError as e:
        abort(400, str(e))

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return jsonify(result=CALCULATOR.multiply(float(op_1), float(op_2)))
    except TypeError as e:
        abort(400, str(e))

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return jsonify(result=CALCULATOR.divide(float(op_1), float(op_2)))
    except TypeError as e:
        abort(400, str(e))

@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return jsonify(result=CALCULATOR.power(float(op_1), float(op_2)))
    except TypeError as e:
        abort(400, str(e))

@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    try:
        num_1 = util.convert_to_number(op_1)
        return jsonify(result=CALCULATOR.sqrt(float(op_1)))
    except TypeError as e:
        abort(400, str(e))

@api_application.route("/calc/log10/<op_1>", methods=["GET"])
def log10(op_1):
    try:
        num_1 = util.convert_to_number(op_1)
        return jsonify(result=CALCULATOR.log10(float(op_1)))
    except TypeError as e:
        abort(400, str(e))
