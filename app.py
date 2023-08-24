from flask import Flask,request

app = Flask(__name__)

lista_alumnos = [{"nombre":"Miguel","mail":"abc@gmail.com","carrera":"Data Science","id":123456},{"nombre":"Juan","mail":"erf@gmail.com","carera":"Ing.Civil","id":987654},{"nombre":"Maria","mail":"poi@gmail.com","carrera":"Ing.Ambiental","id":90345345}]

@app.route('/lista_alumnos',methods = ['GET'])  # Implementacion del method GET
def Mostrar_Alumnos():
    return lista_alumnos
@app.route('/lista_alumnos/<nombre>',methods = ["GET"])   # Implementacion del method GET para un dato especifico de mi lista de diccionario
def Alumno(nombre):
    alumno_encontrado = ""
    for alumno in lista_alumnos:
        if alumno["nombre"] == nombre:
            alumno_encontrado = alumno
            break
    if alumno_encontrado:
        return alumno_encontrado
    else:
        return "Nombre no encontrado"
@app.route('/lista_alumnos',methods=['POST']) #Implementacion del metodo POST
def Agregar_Alumno():
    nuevo_alumno = request.get_json()
    lista_alumnos.append(nuevo_alumno)
    return lista_alumnos

@app.route('/lista_alumnos/<nombre>',methods=["DELETE"]) #Implementacion del metodo DELETE
def Eliminar_Alumno(nombre):
    global lista_alumnos
    Alumno_eliminado = ""
    for alumno in lista_alumnos:
        if alumno["nombre"] == nombre:
            Alumno_eliminado = alumno
            break
    if Alumno_eliminado:
        return lista_alumnos.remove(Alumno_eliminado)
    else:
        return "Nombre no encontrado"


if __name__ == '__main__':
    app.run(debug=True)
