import sqlite3
from flask import render_template
from flask_restful import Resource, reqparse

class QuotesForm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quotefrom',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('quote',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        data = QuotesForm.parser.parse_args()

        query = "INSERT INTO quotes VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['quotefrom'], data['quote']))

        connection.commit()
        connection.close()

        return {"message":"Quote Create Successfully"}, 201

class QuotesGetter(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM quotes"
        result = cursor.execute(query)
        the_array = []
        for row in result:
            the_array.append( [row[1], row[2]] )
        print(the_array)
        return the_array
