def menu_prnicipal():
    print("\n**conversão de unidades**")
    print("1. converte comprimento")
    print("3. sair")

    opcao = input("Digite uma das opcoes: ")
    return opcao

def sair():
    print('O programa terminou')

escolha = menu_prnicipal()  

if escolha == '3':
    sair()