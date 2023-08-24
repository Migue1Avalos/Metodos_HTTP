from flask import Flask

app = Flask(__name__)

alumnos = [{"nombre":"Miguel","carrera":"Data Science","id":123456},{"nombre":"Juan","carera":"Ing.Civil","id":987654},{"nombre":"Maria","carrera":"Ing.Ambiental","id":90345345}]



@app.route('/')
def alumno():  # put application's code here
    return "Hello"

if __name__ == '__main__':
    app.run()
