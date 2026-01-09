print("=== SISTEMA DE LOGIN ===")

usuario_correto = "admin"
senha_correta = "senha123"

tentativas = 3

while tentativas > 0:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("\nLogin bem-sucedido!")

        
        opcao = input("""
Deseja alterar seus dados?
1 - Sim
2 - Não
: """)

        if opcao == '1':
            usuario_correto = input("Novo nome de usuário: ")
            senha_correta = input("Nova senha: ")
            print("Dados alterados com sucesso!")
        else:
            print("Acesso liberado!")

        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}\n")

if tentativas == 0:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
