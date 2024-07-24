from flask import Flask , render_template, request
from arquivo import obter_usuario,salvar_usuario, salvar_sala , obter_salas , salvar_reserva, substituir_csv_salas, obter_reservas
from datetime import datetime

formato_data_hora = '%d/%m/%Y - %H:%M' # exemplo: 30/04/2024 - 16:30

app = Flask("Reserva-App") 

tipos_salas = {
    "1" : "Laboratório de Informática",
    "2" : "Laboratório de Química",
    "3" : "Sala de Aula"
}

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
    return render_template("listar-salas.html" , salas = obter_salas() )

@app.route("/reservar-sala")
def reservarsala(): 
    return render_template("reservar-sala.html", salas = obter_salas())

@app.route("/reservas")
def reservas(): 
    return render_template("reservas.html")

@app.route("/detalhe-reserva")
def  detalhe_reserva(): 
    return render_template("reserva/detalhe-reserva.html")

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
        if (email == usuario['email']) and (password == usuario['password']):
            contem = True
              
    if contem: 
        return render_template ("reservas.html")
    else: 
        return render_template ("login.html")

#cadastrar novo usuário
@app.route("/cadastro", methods = ['POST'])
def cadastrar():
    usuarios = obter_usuario()
    codigo = (len(usuarios))+1
    nome = request.form['nome'].strip()
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    admin = False
    salvar_usuario(codigo,nome,email,password, admin)
    return render_template("login.html")

@app.route("/cadastrar-sala", methods = ['POST'])
def cadastrar_sala():
    salas =  obter_salas()
    codigo = (len(salas))+1
    tipo = request.form['tipo'].strip()
    nome_tipo = tipos_salas[str(tipo)]
    capacidade = request.form['capacidade'].strip()
    descricao = request.form['descricao'].strip()
    salvar_sala(codigo,nome_tipo,capacidade,descricao,"Sim")
    return render_template("listar-salas.html" , salas = obter_salas() )


@app.route("/reservar-sala", methods = ['POST'])
def reservar_sala():
    reservas = obter_reservas()
    codigo = len(reservas)+1
    sala = request.form['sala'].strip()
    inicio = datetime.strptime(request.form['inicio'].strip(), '%Y-%m-%dT%H:%M') 
    fim = datetime.strptime(request.form['fim'].strip(), '%Y-%m-%dT%H:%M') 

    inicio_formatado = inicio.strftime(formato_data_hora)
    fim_formatado = fim.strftime(formato_data_hora)

    salvar_reserva(codigo,sala,inicio_formatado,fim_formatado, "Usuário padrão")

    reserva_atual = {
        "codigo" : codigo,
        "sala": sala,
        "inicio":inicio_formatado,
        "fim": fim_formatado,
        "usuario": "Usuário padrão"
    }
    
    return render_template("reserva/detalhe-reserva.html", reserva = reserva_atual)


@app.route("/editar", methods = ['POST'])
def editar_sala(): 
    return render_template("login.html")


@app.route("/desativar", methods = ['POST'])
def desativar_sala():
    id = 1 # id padrão
    salas = obter_salas()
    salas[id]['ativa'] = "Não"
    substituir_csv_salas(salas)
    return render_template("listar-salas.html", salas = obter_salas())

@app.route("/excluir", methods = ['POST'])
def excluir_sala(): 
    return render_template("login.html")


app.run()