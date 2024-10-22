
def obter_usuario(con):
    cursor = con.cursor()
    sql = "SELECT * FROM Usuario"
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    usuarios = []

    for (registro) in cursor:
        usuarios.append(registro)

    return usuarios
    
def obter_salas(con):
    cursor = con.cursor()
    sql = "SELECT * FROM Sala"
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    salas = []

    for (registro) in cursor:
        salas.append(registro)

    return salas
    
def obter_reservas(con):
    cursor = con.cursor()
    sql = "SELECT * FROM Reserva"
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    reservas = []

    for (registro) in cursor:
        reservas.append(registro)

    return reservas
    

def salvar_usuario(con, nome, email, password, admin):
    cursor = con.cursor()
    sql = "INSERT INTO Usuario (nome, email, password, admin) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, email, password, admin))

    con.commit() 
    cursor.close()


def salvar_sala(con, tipo, capacidade, descricao, ativa):
    cursor = con.cursor()
    sql = "INSERT INTO Sala (tipo, capacidade, descricao, ativa) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql,(tipo, capacidade, descricao, ativa))

    con.commit() 
    cursor.close()

def salvar_reserva(con, sala, usuario, inicio, fim):
    cursor = con.cursor()
    sql = "INSERT INTO Reserva (fk_Sala_idSala, fk_Usuario_idUsuario, inicio, fim) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql,(sala, usuario, inicio, fim))

    con.commit() 
    cursor.close()


        
    