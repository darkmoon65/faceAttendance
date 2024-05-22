from app import app
from usuarios import usuarios

app.register_blueprint(usuarios)

if __name__ == '__main__':
    app.run(port=3000, debug=True)