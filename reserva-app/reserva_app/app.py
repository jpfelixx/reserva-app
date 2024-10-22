from flask import Flask , render_template, request
from arquivo import obter_usuario,salvar_usuario, salvar_sala , obter_salas , salvar_reserva, obter_reservas
from datetime import datetime
from conexao import conexao_fechar, conexao_abrir

formato_data_hora = '%Y-%m-%d %H:%M:%S'

app = Flask("Reserva-App") 
con = conexao_abrir("localhost", "estudante1", "estudante1", "reserva_app")

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
    return render_template("listar-salas.html" , salas = obter_salas(con) )

@app.route("/reservar-sala")
def reservarsala(): 
    return render_template("reservar-sala.html", salas = obter_salas(con))
  
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
    usuarios = obter_usuario(con)
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
    nome = request.form['nome'].strip()
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    admin = False
    salvar_usuario(con, nome,email,password, admin)
    return render_template("login.html")

@app.route("/cadastrar-sala", methods = ['POST'])
def cadastrar_sala():
    tipo = request.form['tipo'].strip()
    nome_tipo = tipos_salas[str(tipo)]
    capacidade = request.form['capacidade'].strip()
    descricao = request.form['descricao'].strip()
    salvar_sala(con, nome_tipo,capacidade,descricao,True)
    return render_template("listar-salas.html" , salas = obter_salas(con) )


@app.route("/reservar-sala", methods = ['POST'])
def reservar_sala():
    usuario = 1 # deveria ser da session
    sala = request.form['sala'].strip()

    # comparar id de sala pra mandar pro bdd

    inicio = datetime.strptime(request.form['inicio'].strip(), '%Y-%m-%dT%H:%M') 
    fim = datetime.strptime(request.form['fim'].strip(), '%Y-%m-%dT%H:%M') 

    inicio_fmt_us = inicio.strftime(formato_data_hora)
    fim_fmt_us = fim.strftime(formato_data_hora)

    salvar_reserva(con, sala, usuario ,inicio_fmt_us, fim_fmt_us)

    # select from
    reserva_atual = {
        "sala": sala,
        "inicio":inicio_fmt_us,
        "fim": fim_fmt_us,
        "usuario": "Usuário padrão"
    }
    
    return render_template("reserva/detalhe-reserva.html", reserva = reserva_atual)


@app.route("/editar", methods = ['POST'])
def editar_sala(): 
    return render_template("login.html")


@app.route("/desativar", methods = ['POST'])
def desativar_sala():
    id = 1 
    salas = obter_salas()
    salas[id]['ativa'] = False
    
    return render_template("listar-salas.html", salas = obter_salas(con))

@app.route("/excluir", methods = ['POST'])
def excluir_sala(): 
    return render_template("login.html")


app.run()

conexao_fechar(con)