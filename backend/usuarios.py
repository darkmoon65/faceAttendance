from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import mysql

usuarios = Blueprint('usuarios', __name__, template_folder='app/templates')


@usuarios.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    return render_template('index.html', usuarios=data)

@usuarios.route('/añadir', methods=['POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        contrasena = request.form['contrasena']
        tipo_usuario_id = request.form['tipo_usuario_id']
        created_at = request.form['created_at']
        usuario_creador = request.form['usuario_creador']
        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO usuarios (username, contrasena, tipo_usuario_id, created_at, usuario_creador) 
            VALUES (%s, %s, %s, %s, %s)
        ''', (username, contrasena, tipo_usuario_id, created_at, usuario_creador))
        mysql.connection.commit()
        flash('Usuario Agregado Correctamente')
        return redirect(url_for('usuarios.Index'))

@usuarios.route('/eliminar/<string:username>')
def eliminar_usuario(username):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE username = %s', [username])
    mysql.connection.commit()
    flash('Usuario Borrado Correctamente')
    return redirect(url_for('usuarios.Index'))

@usuarios.route('/editar/<username>')
def editar_usuario(username):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE username = %s', [username])
    data = cur.fetchall()
    return render_template('edit-usuario.html', usuario=data[0])

@usuarios.route('/actualizar/<username>', methods=['POST'])
def actualizar_usuario(username):
    if request.method == 'POST':
        new_username = request.form['username']
        contrasena = request.form['contrasena']
        tipo_usuario_id = request.form['tipo_usuario_id']
        created_at = request.form['created_at']
        usuario_creador = request.form['usuario_creador']
        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE usuarios
            SET username = %s, contrasena = %s, tipo_usuario_id = %s, created_at = %s, usuario_creador = %s
            WHERE username = %s
        ''', (new_username, contrasena, tipo_usuario_id, created_at, usuario_creador, username))
        mysql.connection.commit()
        flash('Usuario Actualizado Correctamente')
        return redirect(url_for('usuarios.Index'))
