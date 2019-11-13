#Item 3
import hashlib

nomeUser = input("Digite o nome de usuário")
senha = input("Digite a senha")
if len(nomeUser) == 4 == len(senha):
    senhaC = hashlib.md5(senha.encode())
    arquivo = open('cadastroseg.txt', 'r')
    dados = arquivo.readlines()
    parte1 = senhaC.hexdigest()[:16]
    parte2 = senhaC.hexdigest()[-16:]
    dados.append(nomeUser + '\n' + parte1+(parte2[::-1]) + '\n')
    arquivo = open('cadastroseg.txt', 'w')
    arquivo.writelines(dados)
    arquivo.close()


else:
    print("senha e nome de usuário deve ter 4 char")
