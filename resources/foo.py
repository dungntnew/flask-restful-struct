from flask_restful import Resource
from helper.ume import log

class Foo(Resource):
  def get(self):
    log("gogo")

  def post(self):
    pass

