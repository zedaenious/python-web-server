from flask import Flask
from flask_restful import Resource, Api, reqparse

# import pandas as pd
# import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
  # methods go here
  pass

class Locations(Resource):
  # methods go here
  pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
  app.run()