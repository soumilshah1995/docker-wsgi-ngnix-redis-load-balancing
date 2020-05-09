
try:
    from flask import Flask
    from flask_restful import Resource, Api
    import sys
    import os
    import json
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
except Exception :
    pass


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def __init__(self):
        self.name = parser.parse_args().get('name', None)
        self.age = parser.parse_args().get('age', None)

    def get(self):

        DATABASENAME = os.getenv("DATABASENAME")

        return json.dumps({
            "Database":DATABASENAME,
            "name":self.name,
            "age":self.age

        })

api.add_resource(HelloWorld, "/fo")
parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help= "Name is required ")
parser.add_argument("age", type=str, help= "age is not mandatory  ")


if __name__ == '__main__':
    app.run(host="0.0.0.0")