def obter_usuario():
    with open("reserva_app/usuario.csv", "r") as arquivo_usuario:
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

def salvar_usuario(nome, email, password):
    print(nome,email,password)
    with open("reserva_app/usuario.csv", "a") as arquivo_usuario2: 
        usuario =  f"{nome},{email},{password}"
        arquivo_usuario2.write(f"\n{usuario}")