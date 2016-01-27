from flask import Flask
from flask_restful import Api
from resources.foo import Foo
from helper.ume import log

app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, '/foo')

# try use helper
log("starting app")

if __name__ == '__main__':
  app.run(debug=True)
