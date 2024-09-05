from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_characters = db.relationship('Favorite_character', backref='user', lazy=True)
    favorite_vehicles = db.relationship('Favorite_vehicle', backref='user', lazy=True)
    favorite_planets = db.relationship('Favorite_planet', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Favorite_character(db.Model):
    # __tablename__ = 'favorite_character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

    def __repr__(self):
        return '<Favorite_character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class Character(db.Model):
    # __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(120), nullable=False)
    mass = db.Column(db.String(120), nullable=False)
    hair_color = db.Column(db.String(120), nullable=False)
    skin_color = db.Column(db.String(120), nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    favorite_characters = db.relationship('Favorite_character', backref='character', lazy=True)
    # planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False) #planet-character
    # vehicles = db.relationship('Vehicles', backref='character', lazy=True) #character-vehicle
    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Favorite_vehicle(db.Model):
    # __tablename__ = 'favorite_vehicle'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    def __repr__(self):
        return '<Favorite_vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }

class Vehicle(db.Model):
    # __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    cost_in_credits = db.Column(db.String(120), nullable=False)
    length = db.Column(db.String(120), nullable=False)
    max_atmosphering_speed = db.Column(db.String(120), nullable=False)
    passangers = db.Column(db.String(120), nullable=False)
    cargo_capacity = db.Column(db.String(120), nullable=False)
    vehicle_class= db.Column(db.String(120), nullable=False)
    manufacturer= db.Column(db.String(120), nullable=False)
    favorite_vehicles = db.relationship('Favorite_vehicle', backref='vehicle', lazy=True)
    # character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False) #character-vehicle
    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "passangers": self.passangers,
            "cargo_capacity": self.cargo_capacity,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer
        }

class Favorite_planet(db.Model):
    # __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    def __repr__(self):
        return '<Favorite_planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class Planet(db.Model):
    # __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    rotation_period = db.Column(db.String(120), nullable=False)
    orbital_period = db.Column(db.String(120), nullable=False)
    diameter = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(120), nullable=False)
    surface_water = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    favorite_planets = db.relationship('Favorite_planet', backref='planet', lazy=True)
    # characters = db.relationship('Character', backref='planet', lazy=True) #planet-character
    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }
    

