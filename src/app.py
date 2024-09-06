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
from models import db, User, Character, Planet, Vehicle, Favorite_character, Favorite_planet, Favorite_vehicle
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

# ---------------------------------------------------------ENDPOINTS-------------------------------------------

#--------------------------------------------users----------------------------------
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

#Obtiene informacion de un solo usuario segun su id
@app.route('/users/<int:id>')
def get_user(id):
    # print(id)
    try:
        query_user = User.query.filter_by(id = id).first()
        # print(query_user.serialize())
        if query_user is None:
            return jsonify({'error': 'User not found'}), 404
        response_body = {
            "msg": "ok",
            "result": query_user.serialize()
        }
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Elimina un usuario por id
@app.route('/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error':'User not found'}), 404
        #Eliminando el usuario de la db
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200

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
    
#--------------------------------------------------------Favoritos---------------------------------
#Obtiene todos los favoritos de un usuario segun su id
@app.route('/favorites/<int:id_user>')
def get_fav(id_user):
    try:
        user = User.query.get(id_user)
        if not user:
            return jsonify({"error": "User not found. Please enter a valid user ID to view their favorites."}), 404
        
        fav_characters = Favorite_character.query.filter_by(user_id = id_user).all()
        fav_planets = Favorite_planet.query.filter_by(user_id = id_user).all()
        fav_vehicles = Favorite_vehicle.query.filter_by(user_id = id_user).all()
        # print(fav_characters)
        favorites_characters = list(map(lambda item: item.serialize(), fav_characters))
        favorites_planets = list(map(lambda item: item.serialize(), fav_planets))
        favorites_vehicles = list(map(lambda item: item.serialize(), fav_vehicles))
        # print(favorites_characters)

        if not favorites_characters and not favorites_planets and not favorites_vehicles:
            return jsonify({'message': 'Favorites not found'}), 404

        response_body = {
            "favorites_characters": favorites_characters,
            "favorites_planets": favorites_planets,
            "favorites_vehicles": favorites_vehicles
        }
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Agregar personajes, planetas y vechiculos favoritos
@app.route('/favorites', methods=['POST'])
def add_favorite():
    try:
        # Obteniendo y guardando el id del body ingresado
        user_id_new = request.json.get("user_id")
        character_id_new = request.json.get("character_id")
        planet_id_new = request.json.get("planet_id")
        vehicle_id_new = request.json.get("vehicle_id")
        
        if not user_id_new:
            return jsonify({"message":"Please enter a user ID"}), 400
        
        if character_id_new:
            #Creando y guardando un nuevo favorito
            new_fav = Favorite_character(user_id = user_id_new, character_id = character_id_new)
            db.session.add(new_fav)
            db.session.commit()
            response_body = new_fav.serialize()
            return jsonify(response_body), 201
        
        elif planet_id_new:
            new_fav = Favorite_planet(user_id = user_id_new, planet_id = planet_id_new)
            db.session.add(new_fav)
            db.session.commit()
            response_body = new_fav.serialize()
            return jsonify(response_body), 201
        
        elif vehicle_id_new:
            new_fav = Favorite_vehicle(user_id=user_id_new, vehicle_id=vehicle_id_new)
            db.session.add(new_fav)
            db.session.commit()
            response_body = new_fav.serialize()
            return jsonify(response_body), 201
        else:
            # mandaste un user id, pero no me mandaste que favoritear
            return jsonify({"message":"You entered the user ID, but you haven't indicated which ID you want to mark as a favorite."}), 400

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Elimina un personaje favorito de cada usuario segun su id
@app.route('/favorite/character/<int:id_user>/<int:id_character>', methods = ['DELETE'])
def delete_fav_character(id_user, id_character):
    try:
        #Verificando que los id ingresados existan para proceder con la busqueda del favorito
        user = User.query.get(id_user)
        character = Character.query.get(id_character)
        if not user or not character:
            return jsonify({"error": "The user or character does not exist. Please enter valid ID values."}), 404
        
        favorite_character = Favorite_character.query.filter_by(user_id = id_user, character_id = id_character).first()
        if not favorite_character:
            return jsonify({'error': 'Character not found in their favorites'}), 404
        
        #Eliminando el favorito de la db
        db.session.delete(favorite_character)
        db.session.commit()
        return jsonify({'message': 'Favorite character deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    
#Elimina un planeta favorito de cada usuario segun su id
@app.route('/favorite/planet/<int:id_user>/<int:id_planet>', methods = ['DELETE'])
def delete_fav_planet(id_user, id_planet):
    try:
        user = User.query.get(id_user)
        planet = Planet.query.get(id_planet)
        if not user or not planet:
            return jsonify({"error": "The user or planet does not exist. Please enter valid ID values."}), 404
        
        favorite_planet = Favorite_planet.query.filter_by(user_id = id_user, planet_id = id_planet).first()
        if not favorite_planet:
            return jsonify({'error':'Planet not found in their favorites'}), 404
        
        db.session.delete(favorite_planet)
        db.session.commit()
        return jsonify({'message': 'Favorite planet deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

#Elimina un vehiculo favorito de cada usuario segun su id
@app.route('/favorite/vehicle/<int:id_user>/<int:id_vehicle>', methods = ['DELETE'])
def delete_fav_vehicle(id_user, id_vehicle):
    try:
        user = User.query.get(id_user)
        vehicle = Vehicle.query.get(id_vehicle)
        if not user or not vehicle:
            return jsonify({"error": "The user or vehicle does not exist. Please enter valid ID values."}), 404

        favorite_vehicle = Favorite_vehicle.query.filter_by(user_id = id_user, vehicle_id = id_vehicle).first()
        if not favorite_vehicle:
            return jsonify({'error':'Vehicle not found in their favorites'}), 404
        
        db.session.delete(favorite_vehicle)
        db.session.commit()
        return jsonify({'message': 'Favorite vehicle deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
