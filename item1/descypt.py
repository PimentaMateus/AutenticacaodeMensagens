#Item 2
from string import ascii_lowercase
from itertools import product
import hashlib
import time
maxrange = 1
def solve_password(password, maxrange):
    charset = ascii_lowercase
    for i in range(maxrange+1):
        for attempt in product(charset, repeat=i):
            if ''.join(attempt) == password:
                return ''.join(attempt)
arq1 = open("cadastro.txt", 'r')
lista1 = []
for line in arq1.readlines():
    lista1.append(line.rstrip())
l1 = lista1[0]
a1 = lista1[1]
l2 = lista1[2]
a2 = lista1[3]
l3 = lista1[4]
a3 = lista1[5]
l4 = lista1[6]
a4 = lista1[7]
separaBlocos = "*****************************"
parada = 0
solved = solve_password('solve', maxrange)
lista = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','¨','&','*','(','+','-',')','Ç','ç','[',']','{','}','~','>','<']
start = time.time()
for possivel_senha in product(lista, repeat=4):
    possivel_senha_string = "".join(possivel_senha)
    possivel_senha_med = hashlib.md5(possivel_senha_string.encode())
    possivel_senha_crip = possivel_senha_med.hexdigest()
    if a1 == possivel_senha_crip:
        parada += 1
        print(f"Login: {l1} \nPossivel senha: {possivel_senha_string} \nHash da senha: {possivel_senha_crip}\n{separaBlocos}")
    if a2 == possivel_senha_crip:
        parada += 1
        print(f"Login: {l2} \nPossivel senha: {possivel_senha_string} \nHash da senha: {possivel_senha_crip}\n{separaBlocos}")
    if a3 == possivel_senha_crip:
        parada += 1
        print(f"Login: {l3} \nPossivel senha: {possivel_senha_string} \nHash da senha: {possivel_senha_crip}\n{separaBlocos}")
    if a4 == possivel_senha_crip:
        parada += 1
        print(f"Login: {l4} \nPossivel senha: {possivel_senha_string} \nHash da senha: {possivel_senha_crip}\n{separaBlocos}")
    if parada >= 4:
        end = (time.time() - start)
        print("Completo")
        print(f"Tempo de execução: {end}")
        break

