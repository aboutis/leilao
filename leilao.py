logo = '''

  _        ______   _____   _                    ____  
 | |      |  ____| |_   _| | |          /\      / __ \ 
 | |      | |__      | |   | |         /  \    | |  | |
 | |      |  __|     | |   | |        / /\ \   | |  | |
 | |____  | |____   _| |_  | |____   / ____ \  | |__| |
 |______| |______| |_____| |______| /_/    \_\  \____/                                   

'''
print(logo)
print("Bem vindo(a) ao leilão.")

inf = {}
repetir = True

def maior(aposta):
    maxi = 0
    ganhador = ""
    for chave in aposta:
        valor = int(aposta[chave])
        if valor > maxi:
            maxi = valor
            ganhador = chave
    print(f"O ganhador(a) é {ganhador.title()} com o lance de RS${maxi}.")

while repetir == True:
    nome = input("Qual o seu nome?: ").lower().strip()
    lance = input("Qual o seu lance?: ")
    inf[nome] = lance
    novo = input("Existem outros compradores? (sim/nao): ").lower().strip()
    if novo == "nao":
        repetir = False
        maior(inf)


