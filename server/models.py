from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

# Table Columns:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
# TBD on whether these will be necessary for API database:
    # dunkability = db.Column(db.String)
    # frequency = db.Column(db.String)
    # skill_level = db.Column(db.String)
# Table Relationships:
    player_games = db.relationship('PlayerGame', back_populates='player', cascade='all, delete-orphan')
    games = association_proxy('player_games', 'game',
        creator=lambda g: PlayerGame(game=g))
    
    def __repr__(self):
        return f"Player # {self.id}: {self.username} player"

class PlayerGame(db.Model, SerializerMixin):
    __tablename__ = 'player_games'

# Table Columns:
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.String)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

# Table Relationships:
    player = db.relationship('Player', back_populates='player_games')
    game = db.relationship('Game', back_populates='player_games')

    def __repr__(self):
        return f"PlayerGame # {self.id}: {self.score}"
    
class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

# Table Columns: 
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, server_default = db.func.now())
    type = db.Column(db.String)
    description = db.Column(db.String)

    court_id = db.Column(db.Integer, db.ForeignKey('courts.id'))

# Table Relationships:
    player_games = db.relationship('PlayerGame', back_populates='game')
    court = db.relationship('Court', back_populates='games')
    players = association_proxy('player_games', 'player', creator=lambda p: PlayerGame(player=p))

    def __repr__(self):
        return f"Game # {self.id}: {self.description} at {self.date_time}."
    
class Court(db.Model, SerializerMixin):
    __tablename__ = 'courts'

# Table Columns:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    location = db.Column(db.String)

# Table Relationships:
    games = db.relationship('Game', back_populates='court', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Court # {self.id}: {self.title} at {self.location}."
    