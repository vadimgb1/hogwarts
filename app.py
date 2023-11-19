from flask import Flask, render_template, redirect, request, session
from flask_session import Session

# Соединение с базой данных
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
url="sqlite:///hogwarts.db"
engine = create_engine(url)
db = scoped_session(sessionmaker(bind=engine))

# конфигурируем приложение
app = Flask(__name__)

# Конфигурируем сессию
app.config["SESSION_PREMANENT"]  = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        row = db.execute(text("select * from 'characters' where username= :username and password=:password"), 
                {"username": username, "password": password}).fetchone()
        if row: 
            session["username"] = row.username
            session["id"] = row.id
            return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["username"] = None
    session["id"] = None
    return redirect("/")



