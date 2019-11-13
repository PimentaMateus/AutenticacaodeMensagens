#Item 1
import hashlib

nomeUser = input("Digite o nome de usuário")
senha = input("Digite a senha")
if len(nomeUser) == 4 == len(senha):
    senhaC = hashlib.md5(senha.encode())
    arquivo = open('cadastro.txt', 'r')
    dados = arquivo.readlines()
    dados.append(nomeUser + '\n' + senhaC.hexdigest() + '\n')
    arquivo = open('cadastro.txt', 'w')
    arquivo.writelines(dados)
    arquivo.close()


else:
    print("senha e nome de usuário deve ter 4 char")
