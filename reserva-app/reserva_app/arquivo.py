def obter_usuario():
    with open("reserva_app/usuario.csv", "r", encoding="utf8") as arquivo_usuario:
        usuarios = []
        for usuario in arquivo_usuario:
            dados_usuario = usuario.strip().split(",")
            usuario ={
                "codigo": dados_usuario[0],
                "nome": dados_usuario[1],
                "email": dados_usuario[2],
                "password": dados_usuario[3],
                "admin": dados_usuario[4]
            }
            usuarios.append(usuario)
        return usuarios
    
def obter_salas():
    with open("reserva_app/salas.csv", "r",encoding="utf8") as arquivo_salas:
        salas = []
        for sala in arquivo_salas:
            dados_sala = sala.strip().split(",")
            sala = {
                "codigo" : dados_sala[0],
                "tipo": dados_sala[1],
                "capacidade": dados_sala[2],
                "descricao": dados_sala[3],
                "ativa": dados_sala[4]
            }

            salas.append(sala)
        return salas
    
def obter_reservas():
    with open("reserva_app/salas.csv", "r",encoding="utf8") as arquivo_reservas:
        reservas = []
        for reserva in arquivo_reservas:
            dados_reserva = reserva.strip().split(",")
            reserva = {
                "codigo" : dados_reserva[0],
                "sala": dados_reserva[1],
                "inicio": dados_reserva[2],
                "fim": dados_reserva[3],
                "usuario": dados_reserva[4]
            }
            reservas.append(reserva)
        return reservas

def salvar_usuario(codigo, nome, email, password, admin):
    with open("reserva_app/usuario.csv", "a", encoding="utf8") as arquivo_usuario: 
        usuario =  f"{codigo},{nome},{email},{password},{admin}"
        arquivo_usuario.write(f"{usuario}\n")

def salvar_sala(codigo, tipo, capacidade, descricao, ativa):
    with open("reserva_app/salas.csv", "a",encoding="utf8") as arquivo_salas: 
        sala =  f"{codigo},{tipo},{capacidade},{descricao},{ativa}"
        arquivo_salas.write(f"{sala}\n")

def salvar_reserva(codigo,sala, inicio, fim, usuario):
    with open("reserva_app/reservas.csv", "a", encoding="utf8") as arquivo_reservas: 
        reserva =  f"{codigo},{sala},{inicio},{fim},{usuario}"
        arquivo_reservas.write(f"{reserva}\n")

def substituir_csv_salas(salas):
    with open("reserva_app/salas.csv", "w", encoding="utf8") as arquivo_salas: 
        for sala in salas:
            linha_sala =  f"{sala['codigo']},{sala['tipo']},{sala['capacidade']},{sala['descricao']},{sala['ativa']}"
            arquivo_salas.write(f"{linha_sala}\n")

         
        
    