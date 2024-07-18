from flask import Flask , render_template, request

app = Flask("Reserva-App") 

@app.route("/")
def login(): 
    return render_template("login.html")

@app.route("/cadastro")
def cadastro(): 
    return render_template("cadastro.html")

@app.route("/cadastrar-sala")
def cadastrarsala(): 
    return render_template("cadastrar-sala.html")

@app.route("/listar-salas")
def listarsalas(): 
    return render_template("listar-salas.html")

@app.route("/reservar-sala")
def reservarsala(): 
    return render_template("reservar-sala.html")

@app.route("/reservas")
def reservas(): 
    return render_template("reservas.html")

#login
@app.route("/", methods = ['POST'])
def entrar():
    email = request.form['email']
    password = request.form['password']
    return render_template ("reservas.html")

app.run()
