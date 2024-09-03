"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# -----------------------------------------Endpoints-----------------------------------
# Obtiene informacion de todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users_results = User.query.all()
        # print(users_results)
        results = list(map(lambda item: item.serialize(), users_results))
        # print(results)
        if results:
            response_body = {
                "msg": "ok",
                "results": results
            }
            return jsonify(response_body), 200
        return jsonify({'error': 'Users not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#------------------------------------Personajes---------------------------------
#Obtiene todos los personajes
@app.route('/characters', methods=['GET'])
def get_characters():
    try:
        characters_results = Character.query.all()
        # print(characters_results)
        results = list(map(lambda item: item.serialize(), characters_results))
        # print(results)
        if results:
            response_body = {
                "msg": "ok",
                "results": results
            }
            return jsonify(response_body), 200
        return jsonify({'error': 'Characters not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Obtiene informacion de un solo personaje segun su id
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    # print(character_id)
    try:
        query_character = Character.query.filter_by(id = character_id).first()
        # print(query_character.serialize())
        if query_character is None:
            return jsonify({'error': 'Character not found'}), 404
        response_body = {
            "msg": "ok",
            "result": query_character.serialize()
        }
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
#------------------------------------Planetas----------------------------------
#Obtiene todos los planetas
@app.route('/planets', methods=['GET'])
def get_planets():
    try:
        planets_results = Planet.query.all()
        # print(planets_results)
        results = list(map(lambda item: item.serialize(), planets_results))
        # print(results)
        if results:
            response_body = {
                "msg": "ok",
                "results": results
            }
            return jsonify(response_body), 200
        return jsonify({'error': 'Planets not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Obtiene informacion de un solo planeta
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    # print(planet_id)
    try:
        query_planet = Planet.query.filter_by(id = planet_id).first()
        # print(query_planet.serialize())
        if query_planet is None:
            return jsonify({'error': 'Planet not found'}), 404
        response_body = {
            "msg": "ok",
            "result": query_planet.serialize()
        }
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
#------------------------------------Vehiculos---------------------------------
#Obtiene todos los planetas
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    try:
        vehicles_results = Vehicle.query.all()
        # print(vehicles_results)
        results = list(map(lambda item: item.serialize(), vehicles_results))
        # print(results)
        if results:
            response_body = {
                "msg": "ok",
                "results": results
            }
            return jsonify(response_body), 200
        return jsonify({'error': 'Vehicles not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    
#Obtiene informacion de un solo vehiculo
@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    # print(vehicle_id)
    try:
        query_vehicle = Vehicle.query.filter_by(id = vehicle_id).first()
        # print(query_vehicle.serialize())
        if query_vehicle is None:
            return jsonify({'error': 'Vehicle not found'}), 404
        response_body = {
            "msg": "ok",
            "result": query_vehicle.serialize()
        }
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

@app.route('/favorites', methods=['POST'])
def add_favorite():
    # try:





# @app.route('/user', methods=['GET'])
# def handle_hello():
#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }
#     return jsonify(response_body), 200

# if vehicle id ..apuntando la tabal donde quiero ir
# si existe character_id 
# elif, elif


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
