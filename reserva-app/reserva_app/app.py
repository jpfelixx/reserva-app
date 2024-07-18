from flask import Flask , render_template, request
from arquivo import obter_usuario,salvar_usuario
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

#login de usuário
@app.route("/", methods = ['POST'])
def entrar():
    #puxando do forms 
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    #pegando do arquivo
    usuarios = obter_usuario()
    contem = False 

    #percorrendo a lista e comparando
    for usuario in usuarios: 
        print('ARQUIVO:',usuario['email'], usuario['password'])
        print('FORMS',email,password)
        if (email==usuario['email']) and (password==usuario['password']):
            contem=True
              
    if contem: 
        return render_template ("reservas.html")
    else: 
        return render_template ("login.html")

#cadastrar novo usuário
@app.route("/cadastro", methods = ['POST'])
def cadastrar():
    nome = request.form['nome'].strip()
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    salvar_usuario(nome,email,password)
    return render_template("login.html")

app.run()