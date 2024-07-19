def obter_usuario():
    with open("reserva_app/usuario.csv", "r", encoding="utf8") as arquivo_usuario:
        usuarios = []
        for usuario in arquivo_usuario:
            dados_usuario = usuario.strip().split(",")
            usuario ={
                "nome": dados_usuario[0],
                "email": dados_usuario[1],
                "password": dados_usuario[2]
            }
            usuarios.append(usuario)
        return usuarios
    
def obter_salas():
    with open("reserva_app/salas.csv", "r",encoding="utf8") as arquivo_salas:
        salas = []
        for sala in arquivo_salas:
            dados_sala = sala.strip().split(",")
            sala = {
                "id" : dados_sala[0],
                "tipo": dados_sala[1],
                "capacidade": dados_sala[2],
                "descricao": dados_sala[3],
                "ativa": dados_sala[4]
            }

            salas.append(sala)
        return salas

def salvar_usuario(nome, email, password):
    with open("reserva_app/usuario.csv", "a", encoding="utf8") as arquivo_usuario2: 
        usuario =  f"{nome},{email},{password}"
        arquivo_usuario2.write(f"{usuario}\n")


def salvar_sala(id,tipo, capacidade, descricao, ativa):
    with open("reserva_app/salas.csv", "a",encoding="utf8") as arquivo_salas: 
        sala =  f"{id},{tipo},{capacidade},{descricao},{ativa}"
        arquivo_salas.write(f"{sala}\n")


def salvar_reserva(sala, inicio, fim):
    with open("reserva_app/reservas.csv", "a", encoding="utf8") as arquivo_reservas: 
        reserva =  f"{sala},{inicio},{fim}"
        arquivo_reservas.write(f"{reserva}\n")