def criar_perfil(nome,idade,cidade):
     print(f"{nome},{idade} anos, {cidade}")

criar_perfil(cidade="Curitiba", nome="Julia", idade=25)
#Julia,25 anos, Curitiba - funciona independente da ordem!

def somar_tudo(*numeros):
    return sum(numeros)
somar_tudo(1,2)
somar_tudo(1,2,3,4)
somar_tudo(10,20,30,40)
