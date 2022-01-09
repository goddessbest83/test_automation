from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/user/<name>')
class FamilyName(Resource):
    def get(self, name):
        return {
            'method' : 'get' + ' ' + name
        }

    def put(self, name):
        return {
            'method' : 'put' + ' ' + name
        }

    def delete(self, name):
        return {
            'method' : 'delete' + ' ' + name
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
