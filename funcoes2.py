def exibir_info(**dados):
    for chave,valor in dados.items():
        print(f"{chave}:{valor}")

#Criamos um dicionário vazio para armazenar as entradas

info_usuario = {}

print("Digite as informações (ou 'sair' na chave para encerrar.): ")
while True:
    chave = input("Nome do campo (ex: profissões): ")
    if chave.lower == 'sair':
        break
    valor = input(f"Valor para {chave}: ")
    info_usuario[chave] = valor

#Usamos