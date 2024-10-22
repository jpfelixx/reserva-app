from conexao import conexao_fechar, conexao_abrir


def obter_usuario(con):
    cursor = con.cursor()
    sql = "SELECT * FROM Usuario"
    # Criando o cursor com a opção de retorno como dicionário   
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    usuarios = []

    for (registro) in cursor:
        usuarios.append(registro)
    return usuarios

def main():
    con = conexao_abrir("localhost", "estudante1", "estudante1", "reserva_app")

    obter_usuario(con)

    conexao_fechar(con)

main()