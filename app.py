from flask import Flask,request,redirect,render_template

app = Flask(__name__)

lista_alumnos = [{"nombre":"Miguel","mail":"abc@gmail.com","carrera":"Data Science","id":123456},{"nombre":"Juan","mail":"erf@gmail.com","carera":"Ing.Civil","id":987654},{"nombre":"Maria","mail":"poi@gmail.com","carrera":"Ing.Ambiental","id":90345345}]



@app.route('/')
def Mostrar():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
