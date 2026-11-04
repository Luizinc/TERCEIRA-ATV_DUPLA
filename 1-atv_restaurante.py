import os
import time
valor = 0
lista_pratos = []

while True:
    os.system('cls')
    print('''
===> BEM VINDO AO TEMPERO DA VOVO <===
1- ADICIONAR PRATOS
2- FECHAR CONTA
3- LISTAR PRATOS
0- EXCLUIR PRATO
    ''')

    pergunta = int(input('selecione a opçao desejada: '))

    match pergunta:
        case 1:
            print('''
    ===> TEMPERO DA VOVO <===
    1- PICANHA ......... R$ 25,00
    2- LASANHA ..........R$ 20,00
    3- STROGNOFF.........R$ 18,00
    4- BIFE ACEBOLADO....R$ 15,00
    5- PAO COM OVO.......R$ 5,00
            ''')
            codigo = int(input("digite a opçao desejada: "))

            match codigo:
                case 1:
                    prato = "Picanha"
                    print("picanha selecionada")
                    valor += 25
                    lista_pratos.append(prato)
                case 2:
                    prato = "Lasanha"
                    print("lasanha selecionada")
                    valor += 20
                    lista_pratos.append(prato)
                case 3:
                    prato = "Strognoff"
                    print('strognoff selecionado')
                    valor += 18
                    lista_pratos.append(prato)
                case 4:
                    prato = "Bife Acebolado"
                    print('bife acebolado selecionado')
                    valor += 15
                    lista_pratos.append(prato)
                case 5:
                    prato = "Pao com Ovo"
                    print('pao com ovo selecionado')
                    valor += 5
                    lista_pratos.append(prato)
                case _:
                    print("codigo invalido")
            

        case 2:
            gorgeta=input('gostaria de pagar os 10% do garçom (S/N)').strip().upper()
            if gorgeta=="S":
                print('ok o garçom ficou feliz')
                time.sleep(1)
                os.system('cls')
                calculo=(valor*0.10)
                valor_gorgeta=valor+calculo
                print(f'''\n===CONTA===
                valor={valor_gorgeta}
                gorgeta={calculo}''')
            else:
                print("ok o garçom ficou triste")
                time.sleep(1)

        case 3:
            ...
        case 0:
            break
        case _:
            print("opção inválida")
    input('\npressione enter para continuar')