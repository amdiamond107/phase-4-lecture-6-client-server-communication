#!/usr/bin/env python3

from app import app
from datetime import datetime
from models import db, Player, PlayerGame, Game, Court 

with app.app_context():
    
    Player.query.delete()
    PlayerGame.query.delete()
    Game.query.delete()
    Court.query.delete()

    players = []
    players.append(Player(username="dishindimes88", age=34, gender="male", height="6 feet 0 inches", weight="200 pounds", position="SG", image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCcBwOU8ObIGXPKNXInNlGSHXUPE1p3ztkQw&usqp=CAU'))
    players.append(Player(username="mace-in-yo-face", age=28, gender="male", height="6 feet 5 inches", weight="225 pounds", position="PF", image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdNXhYk1U5pnioghzq2MyWqJl5XA_0lZ38Ng&usqp=CAU'))
    players.append(Player(username="dunkmasterflex", age=25, gender="male", height="6 feet 9 inches", weight="250 pounds", position="C", image='https://thumbs.dreamstime.com/b/street-ball-basketball-streetballer-dunk-942736.jpg'))

    player_games = []
    player_games.append(PlayerGame(score="100-99"))
    player_games.append(PlayerGame(score="88-85"))
    player_games.append(PlayerGame(score="94-89"))

    games = []
    games.append(Game(date_time=datetime(2023, 9, 9, 19, 0 ,0), type="indoors", description="Advanced Men-Only 5-on-5"))
    games.append(Game(date_time=datetime(2023, 8, 8, 19, 0 ,0), type="indoors", description="Intermediate Women-Only 5-on-5"))
    games.append(Game(date_time=datetime(2023, 10, 7, 19, 0 ,0), type="outdoors", description="Recreational co-ed 3-on-3"))

    courts = []
    courts.append(Court(title="PS 6 Gym", location="45 East 81st St, New York, NY, 10028"))
    courts.append(Court(title="Columbia Prep Gym", location="5 West 93rd St, New York, NY, 10025"))
    courts.append(Court(title="Holcombe Rucker Park", location="West 155th St, New York, NY, 10039"))

    db.session.add_all(players)
    db.session.add_all(player_games)
    db.session.add_all(games)
    db.session.add_all(courts)
    db.session.commit()
    print("🌱 Players, Player Games, Games, and Courts successfully seeded! 🌱")
