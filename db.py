from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
url="sqlite:///hogwarts.db"
engine = create_engine(url)
db = scoped_session(sessionmaker(bind=engine))

username = input("user name: ")
password = input("password: ")
character = db.execute(text("select * from 'characters' where username = :username and password = :password"),  
        {"username": username, "password": password}).fetchone()
if character:
    print(f"{character.username} {character.password}")
else:
    print("Ups")

