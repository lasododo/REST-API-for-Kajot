import sqlite3
from flask_restful import Resource, reqparse

class BlogForm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('post',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('user',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        data = BlogForm.parser.parse_args()

        query = "INSERT INTO posts VALUES (NULL, ?, ?, ?)"
        cursor.execute(query, (data['title'], data['post'], data['user']))

        connection.commit()
        connection.close()

        return {"message":"Quote Create Successfully"}, 201

class PostsGetter(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM posts"
        result = cursor.execute(query)
        the_array = []
        for row in result:
            the_array.append( [ row[1], row[2], row[3] ] )
        print(the_array)
        return the_array
