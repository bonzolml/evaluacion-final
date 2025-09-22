from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# Ejercicio 1 
@app.route('/ejercicio1', methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template("resultado1.html",
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento,
                               descuento=int(descuento * 100))
    return render_template("ejercicio1.html")

# Ejercicio 2 
@app.route('/ejercicio2', methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario == "juan" and clave == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and clave == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("resultado2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == '__main__':
    app.run(debug=True)
