from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

cars = {
    1: {"model": "Honda", "color": "White", "sold": 0},
    2: {"model": "Toyota", "color": "Yellow", "sold": 0},
    3: {"model": "BMW", "color": "Black", "sold": 0},
    4: {"model": "Lada", "color": "Red", "sold": 0},
    5: {"model": "Kia", "color": "Blue", "sold": 0},
}

parser = reqparse.RequestParser()
parser.add_argument("model", type=str)
parser.add_argument("color", type=str)
parser.add_argument("sold", type=int)


class Main(Resource):
    def get(self, car_id):
        if car_id == 0:
            return cars
        else:
            return cars[car_id]

    def delete(self, car_id):
        del cars[car_id]
        return cars

    def post(self, car_id):
        cars[car_id] = parser.parse_args()
        return cars

    def put(self, car_id):
        cars[car_id] = parser.parse_args()
        return cars


api.add_resource(Main, "/api/cars/<int:car_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
