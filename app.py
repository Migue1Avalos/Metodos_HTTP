from flask import Flask,request,redirect,render_template

app = Flask(__name__)

lista_alumnos = [{"nombre":"Miguel","mail":"abc@gmail.com","carrera":"Data Science","id":123456},{"nombre":"Juan","mail":"erf@gmail.com","carera":"Ing.Civil","id":987654},{"nombre":"Maria","mail":"poi@gmail.com","carrera":"Ing.Ambiental","id":90345345}]



@app.route('/',methods = ['GET'])
def Registro():
    return render_template("index.html")
@app.route('/registro',methods = ['POST'])
def Mostrar_Registro():
    name = request.form.get("name")
    mail = request.form.get("mail")
    carrera = request.form.get("carrera")
    id = request.form.get("id")
    if not name or not carrera or not mail or not id:
        return render_template("Error.html")
    lista_alumnos.append(f"Registered: {name};  {mail};  {carrera}; {id}")
    return redirect("/registro_alumnos")
@app.route('/registros_alumnos')
def registrantes():
    return render_template("registrados.html", lista_alumnos = lista_alumnos)





if __name__ == '__main__':
    app.run()
