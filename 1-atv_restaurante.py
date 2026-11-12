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
4- EXCLUIR PRATO
5- ATUALIZAR PRATO
    ''')

    # Tratamento para evitar erro caso digitem letras no menu principal
    opcao_str = input('selecione a opçao desejada: ')
    if not opcao_str.isdigit():
        print("Opção inválida! Digite apenas números.")
        input('\nPressione Enter para continuar')
        continue
    
    pergunta = int(opcao_str)
    os.system('cls')

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
            
            codigo_str = input("digite a opçao desejada: ")
            if not codigo_str.isdigit():
                print("Código inválido!")
            else:
                codigo = int(codigo_str)
                match codigo:
                    case 1:
                        prato = "Picanha"
                        print("Picanha selecionada")
                        valor += 25
                        lista_pratos.append(prato)
                    case 2:
                        prato = "Lasanha"
                        print("Lasanha selecionada")
                        valor += 20
                        lista_pratos.append(prato)
                    case 3:
                        prato = "Strognoff"
                        print('Strognoff selecionado')
                        valor += 18
                        lista_pratos.append(prato)
                    case 4:
                        prato = "Bife Acebolado"
                        print('Bife acebolado selecionado')
                        valor += 15
                        lista_pratos.append(prato)
                    case 5:
                        prato = "Pao com Ovo"
                        print('Pao com ovo selecionado')
                        valor += 5
                        lista_pratos.append(prato)
                    case _:
                        print("Código de prato inválido!")

        case 2:
            gorgeta = input('gostaria de pagar os 10% do garçom (S/N): ').strip().upper()
            if gorgeta == "S":
                print('ok, o garçom ficou feliz!')
                time.sleep(1)
                os.system('cls')
                calculo = (valor * 0.10)
                valor_gorgeta = valor + calculo
                print(f'\n=== CONTA ===')
                print(f'Valor total com 10%: R$ {valor_gorgeta:.2f}')
                break
            else:
                print("ok, o garçom ficou triste...")
                time.sleep(1)
                os.system('cls')
                print(f'\n=== CONTA ===')
                print(f'Valor total: R$ {valor:.2f}')
                break

        case 3:
            print("=== PRATOS ADICIONADOS ===")
            if not lista_pratos:
                print("Nenhum prato na lista ainda.")
            else:
                for prato in lista_pratos:
                    print(f"- {prato}")

        case 4:
            print("=== EXCLUIR PRATO ===")
            prato_apagar = input("digite o nome do prato que deseja apagar: ").strip().lower()
            
            prato_encontrado = None
            for prato in lista_pratos:
                if prato.strip().lower() == prato_apagar:
                    prato_encontrado = prato
                    break
                    
            if prato_encontrado:
                lista_pratos.remove(prato_encontrado)
                
                # Subtrai o valor correto do prato removido
                if prato_encontrado == "Picanha":
                    valor -= 25
                elif prato_encontrado == "Lasanha":
                    valor -= 20
                elif prato_encontrado == "Strognoff":
                    valor -= 18
                elif prato_encontrado == "Bife Acebolado":
                    valor -= 15
                elif prato_encontrado == "Pao com Ovo":
                    valor -= 5
                    
                print(f"Prato '{prato_encontrado}' removido com sucesso!")
            else:
                print(f"Prato '{prato_apagar}' não encontrado na lista.")

        case 5:
            print("=== ATUALIZAR PRATO ===")
            prato_atualizar = input("digite o nome do prato que deseja atualizar: ").strip().lower()
            
            indice_encontrado = -1
            for i, prato in enumerate(lista_pratos):
                if prato.strip().lower() == prato_atualizar:
                    indice_encontrado = i
                    break
                    
            if indice_encontrado != -1:
                nome_antigo = lista_pratos[indice_encontrado]
                
                print("\nEscolha o novo prato:")
                print("1- Picanha (R$ 25)")
                print("2- Lasanha (R$ 20)")
                print("3- Strognoff (R$ 18)")
                print("4- Bife Acebolado (R$ 15)")
                print("5- Pao com Ovo (R$ 5)")
                
                novo_codigo_str = input("Digite o número da nova opção: ")
                if novo_codigo_str.isdigit():
                    novo_codigo = int(novo_codigo_str)
                    
                    # Subtrai o valor antigo
                    if nome_antigo == "Picanha": valor -= 25
                    elif nome_antigo == "Lasanha": valor -= 20
                    elif nome_antigo == "Strognoff": valor -= 18
                    elif nome_antigo == "Bife Acebolado": valor -= 15
                    elif nome_antigo == "Pao com Ovo": valor -= 5

                    # Atualiza o nome e adiciona o novo valor
                    if novo_codigo == 1:
                        novo_prato = "Picanha"
                        valor += 25
                    elif novo_codigo == 2:
                        novo_prato = "Lasanha"
                        valor += 20
                    elif novo_codigo == 3:
                        novo_prato = "Strognoff"
                        valor += 18
                    elif novo_codigo == 4:
                        novo_prato = "Bife Acebolado"
                        valor += 15
                    elif novo_codigo == 5:
                        novo_prato = "Pao com Ovo"
                        valor += 5
                    else:
                        print("Opção inválida, atualização cancelada.")
                        # Devolve o valor antigo caso cancele
                        if nome_antigo == "Picanha": valor += 25
                        elif nome_antigo == "Lasanha": valor += 20
                        elif nome_antigo == "Strognoff": valor += 18
                        elif nome_antigo == "Bife Acebolado": valor += 15
                        elif nome_antigo == "Pao com Ovo": valor += 5
                        input('\nPressione Enter para continuar')
                        continue

                    lista_pratos[indice_encontrado] = novo_prato
                    print(f"Prato '{nome_antigo}' atualizado para '{novo_prato}' com sucesso!")
                else:
                    print("Entrada inválida.")
            else:
                print(f"Prato '{prato_atualizar}' não encontrado na lista.")

        case _:
            print("Opção inválida!")

    input('\nPressione Enter para continuar')
