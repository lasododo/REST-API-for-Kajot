from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import requests
import json
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)

class Quotes():
    def __init__(self, quote, user):
        self.quote = quote
        self.user = user

class Posts():
    def __init__(self,title ,post, user):
        self.title = title
        self.post = post
        self.user = user


@app.route('/')
def get():
    return render_template("Home.html")

@app.route('/quotes/send')
def get_quotes_to_send():
    return render_template("SendQuote.html")

@app.route('/quotes')
def get_quotes():
    url = "http://127.0.0.1:5000/quotes"
    f = urllib.request.urlopen(url)
    the_html = f.read()
    quotes = BeautifulSoup(the_html, "lxml").text
    quotes = quotes.replace("[", "")
    quotes = quotes.replace("]", "")
    quotes = quotes.replace("\n", "")
    quotes = quotes.strip()
    quotes = quotes.split(',')
    useful_var = 0
    counter = 0
    obj_array = []
    for stuff in quotes:
        if counter == 0:
            useful_var = stuff
            counter += 1
        else:
            item = Quotes(useful_var, stuff)
            obj_array.append(item)
            useful_var = 0
            counter = 0
    print(obj_array)
    return render_template("QuotesSite.html", quotes=obj_array)

@app.route('/blog/send')
def get_blog_to_send():
    return render_template("SendPost.html")

@app.route('/blog')
def get_blog():
    url = "http://127.0.0.1:5000/blog"
    f = urllib.request.urlopen(url)
    the_html = f.read()
    quotes = BeautifulSoup(the_html, "lxml").text
    quotes = quotes.replace("[", "")
    quotes = quotes.replace("]", "")
    quotes = quotes.replace("\n", "")
    quotes = quotes.strip()
    quotes = quotes.split(',')
    useful_var = 0
    useful_var2 = 0
    counter = 0
    obj_array = []
    for stuff in quotes:
        if counter == 0:
            useful_var = stuff
            useful_var = useful_var.replace('"', "")
            counter += 1
        if counter == 1:
            useful_var2 = stuff
            useful_var2 = useful_var2.replace('"', "")
            counter += 1
        else:
            item = Posts(useful_var, useful_var2, stuff)
            obj_array.append(item)
            useful_var = 0
            counter = 0
    print(obj_array)
    return render_template("RandomPosts.html", quotes=obj_array)

@app.route('/login')
def get_login():
    return render_template("SignIn.html")

@app.route('/signup')
def get_signup():
    return render_template("SignUp.html")

app.run(port=5500, debug=True)
