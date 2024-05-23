from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.mysql_connection_pool import MySQLPool

usuarios = Blueprint('usuarios', __name__, template_folder='app/templates')

class usuarioModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_all(self):
        rv = self.mysql_pool.execute("SELECT * FROM usuarios")
        data = []
        content = {}
        for result in rv:
            content = {
                'username': result[0],
                'contrasena': result[1],
                'tipo_usuario_id': result[2],
                'created_at': result[3],
                'usuario_creador': result[4],
            }
            data.append(content)
            content = {}
        return data
    
    def create_usuario(
        self, 
        username,
        contrasena,
        tipo_usuario_id,
        created_at,
        usuario_creador
    ):
        data = {
            'username' : username,
            'contrasena' : contrasena,
            'tipo_usuario_id' : tipo_usuario_id,
            'created_at': created_at,
            'usuario_creador': usuario_creador,
        }
        query = """  INSERT INTO usuarios (username, contrasena, tipo_usuario_id, created_at, usuario_creador) 
                VALUES (%(username)s, %(contrasena)s, %(tipo_usuario_id)s, %(created_at)s, %(usuario_creador)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def actualizar_usuario(
        self, 
        username,
        contrasena,
        tipo_usuario_id,
        created_at,
        usuario_creador
    ):
        data = {
            'username' : username,
            'contrasena' : contrasena,
            'tipo_usuario_id' : tipo_usuario_id,
            'created_at': created_at,
            'usuario_creador': usuario_creador,
        }
        query = """ UPDATE usuarios
                SET username = %(username)s, contrasena = %(contrasena)s, 
                tipo_usuario_id = %(tipo_usuario_id)s, created_at = %(created_at)s, 
                usuario_creador = %(usuario_creador)s
                WHERE username = %(username)s"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def eliminar_usuario(self, username):
        params = {'username': username}
        query = """ DELETE FROM usuarios WHERE username = %(username)s """
        self.mysql_pool.execute(query, params, commit=True)  

        result = {'result': 1}
        return result
