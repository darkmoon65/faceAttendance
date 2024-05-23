from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from blueprints.usuario_blueprint import usuario_blueprint

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Clave'
jwt = JWTManager(app)
cors = CORS(app)

app.register_blueprint(usuario_blueprint)


if __name__ == "__main__":
    app.run(port=4000, debug=True)