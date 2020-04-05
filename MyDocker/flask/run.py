from flask import Flask
from flask_restful import Resource, Api
import sys
import os
import json
import redis


app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]


class HelloWorld(Resource):
    def get(self):
        r = redis.Redis(host='redis', port=6379, db=0)
        if r.ping():
            message = "Redis Ok "
        else:
            message = "Failed ..."
        return json.dumps({"Message":"ok : {}".format(message)})


api.add_resource(HelloWorld, '/fo')


if __name__ == '__main__':
    app.run(host="0.0.0.0")