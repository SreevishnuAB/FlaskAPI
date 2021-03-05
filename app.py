from flask import Flask, json, jsonify, request
from sqlalchemy.sql import select

from db.config import Database
from model.car import Car

app = Flask(__name__)

engine = Database().engine


@app.route("/", methods=['GET'])
def test_route():
  return jsonify({"details": "Hello World"})

@app.route('/car', methods=['POST'])
def create_car():
  car = request.data.decode("UTF-8")
  car = json.loads(car)
  app.logger.debug(car)
  query = Car.insert().values(name=car["name"], year=car["year"])
  with engine.connect() as conn:
    conn.execute(query)
  return {"detail": "Car created"}, 201

@app.route("/car", methods=['GET'])
def get_cars():
  query = select([Car])
  with engine.connect() as conn:
    res = conn.execute(query)
    # app.logger.debug(list(res))
    # for item in list(res):
    #   app.logger.debug(item[0], item[1], item[2])
    response = [{"id": _item[0], "name": _item[1], "year": _item[2]} for _item in list(res)]
    # app.logger.debug(response)
    return jsonify({"data": response}), 200