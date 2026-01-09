#login simples

usuario_correto = "admin"
senha_correta = "senha123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
   print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")

#login com tentativas limitadas

usuario_correto = "admin"
senha_correta = "senha123"

tentativas = 3
while tentativas > 0:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        tentativas -= 1
        print(f"Nome de usuário ou senha incorretos. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")

#login com criação de senha

usuario_correto = "admin"
senha_correta = "senha123"

nova_senha = input("Crie uma nova senha: ")

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == nova_senha:
    print("Login bem-sucedido!")
    senha = nova_senha
    print("Senha alterada com sucesso!")
else:
    print("Nome de usuário ou senha incorretos.")

#login com opção de alterar dados

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

alterar = input("""Deseja alterar seus dados? 
1 - Sim   2 - Não  
: """)

if alterar == '1':
    usuario_novo = input("Crie um nome de usuário: ")
    senha_nova = input("Crie uma nova senha: ")
    print("Dados alterados com sucesso!")
elif alterar == '2':
    print("Acesso Liberado!")
else:
    print("Opção inválida.") 



