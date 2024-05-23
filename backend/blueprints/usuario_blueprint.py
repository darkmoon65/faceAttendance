from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_cors import CORS, cross_origin 

from models.usuario_model import usuarioModel;
model = usuarioModel()

usuario_blueprint = Blueprint('usuarios', __name__)

@usuario_blueprint.route('/')
@cross_origin()
def get_all():
    return jsonify(model.get_all())

@usuario_blueprint.route('/agregar', methods=['POST'])
@cross_origin()
def add():
    username = request.json['username']
    contrasena = request.json['contrasena']
    tipo_usuario_id = request.json['tipo_usuario_id']
    created_at = request.json['created_at']
    usuario_creador = request.json['usuario_creador']

    content = model.create_usuario(username, contrasena, tipo_usuario_id, created_at, usuario_creador)
    return jsonify(content)

@usuario_blueprint.route('/eliminar/<string:username>')
@cross_origin()
def eliminar_usuario(username):
    return jsonify(model.eliminar_usuario(username))

# @usuarios.route('/editar/<username>')
# @cross_origin()
# def get_by_id(username):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM usuarios WHERE username = %s', [username])
#     data = cur.fetchall()
#     return render_template('edit-usuario.html', usuario=data[0])

@usuario_blueprint.route('/actualizar/<username>', methods=['POST'])
@cross_origin()
def actualizar_usuario(username):
    username = request.json['username']
    contrasena = request.json['contrasena']
    tipo_usuario_id = request.json['tipo_usuario_id']
    created_at = request.json['created_at']
    usuario_creador = request.json['usuario_creador']

    content = model.actualizar_usuario(username, contrasena, tipo_usuario_id, created_at, usuario_creador)
    return jsonify(content)
