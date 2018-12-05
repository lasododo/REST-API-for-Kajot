from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import requests
import json

# Vsetky z vyssie uvedenych importov som vyuzil ( v priprave na tento projekt ), no nevedel som si moc pomoct s API, tak som to skusil takto.
# Dufam ze to nieje neako moc zle ( ucil som sa z tutorialu, kde boli vytvarane len cisto API a testovane boli
# cez program postman ... Dostal som predstavu otom ako sa API robia, no potom som narazil na problem s
# Front-Endom ... bohuzial kedze ma tlaci cas, tak musim vyuzit toto, nie moc pekne riesenie ( zaroven som
# nikde nenasiel ako realne spravit komunikaciu medzi front-endom a API ... to iste s Flaskom .. teda az
# na tu vo form, kde je action= , inak som skusal aj jsonify a requests, no hadzalo to privela errorov :(    )))

from security import authenticate, identity
from user import UserRegister
from quote import QuotesForm, QuotesGetter
from blogpost import BlogForm, PostsGetter

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(QuotesForm, '/quotes/posts')
api.add_resource(BlogForm, '/blog/posts')
api.add_resource(QuotesGetter, '/quotes')
api.add_resource(PostsGetter, '/blog')

app.run(port=5000, debug=True)
