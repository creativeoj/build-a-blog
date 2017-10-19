from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key ='random string'
app.config['SQLALCHEMY_DATABASE_URI'] 'mysql+pymysql://build-a-blog:buildablog@localhose:8889/build-a-blog'
app.config['AQLALCHEMY_ECHO'] =True
db=AQLAlchemy(app)

class Blog(db.Model):
    id = db.Colume(db.Inteader, primary_key =turtles()