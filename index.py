from flask import Flask, render_template, request  # llama al framework
# agrega el metodo de flask para utilizar lo que hay dentro de la carpeta templates

app = Flask(__name__)  # guarda en una variable la ruta de inicio de la app

# Rutas de procesamiento (direccionan a algun lugar)
@app.route('/')  # método que crea una url
def home():      # función  que devuelve información al navegador
    # retorna el archivo dentro de la carpeta templates
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contacts')
def contacts():
    #return render_template("contact.html")
    success = request.args.get('success') == 'true'
    return render_template("contact.html", success=success)


@app.route('/validar')
def validar():
    return render_template("validar.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/alumnos')
def alumnos():
    return render_template("alumnos.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/courses')
def courses():
    return render_template("courses.html")


# validamos si estamos en el archivo principal para que siempre se quede
# escuchando una peticion del usuario y si se cumple ejecuta el app.run
if __name__ == '__main__':
    app.run(debug=True)   # avisamos que estamos en un entorno de prueba
    # y se actualiza el servidor automáticamente....
