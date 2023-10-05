
print("---------------------------")
print("  DEPARTAMENTO DE TRANSITO ")
print("---------------------------")
idade = int(input('Em que ano você nasceu ?'))
ano = int(input('Qual o ano em que estamos?'))
sub = ano-idade

if sub >= 18:
    print("-------------STATUS------------")
    print("Idade", sub, " Anos")
    print("Você ATINGIU a idade mínima para tirar carteira!")
    print("-------------------------------")
else:
    print("----------------STATUS---------------")
    print("Idade", sub, " Anos")
    print("Você  NÃO atingiu a idade mínima para tirar carteira!")
    print("-------------------------------------")
