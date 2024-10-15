from pousada import Pousada
from quarto import Quarto
from reserva import Reserva
from produto import Produto

# Criando o método main para reproduzir o menu
def main():

    # Criando a instância pousada
    pousada = Pousada('Pousada Salem e Pesca', '@salemepesca')

    # Criando as instâncias dos quartos
    quarto1 = Quarto(1, 100.0, 'S', 'L')
    quarto2 = Quarto(2, 200.0, 'S', 'L')
    quarto3 = Quarto(3, 300.0, 'M', 'L')
    quarto4 = Quarto(4, 400.0, 'M', 'L')
    quarto5 = Quarto(5, 500.0, 'P', 'L')
    quarto6 = Quarto(6, 600.0, 'P', 'L')

    # Adicionando as instâncias dos quartos na pousada
    pousada.quarto.extend([quarto1, quarto2, quarto3, quarto4, quarto5, quarto6])

    # Criando as instâncias dos produtos
    produto1 = Produto(1, "Café", 5.0)
    produto2 = Produto(2, "Água", 2.0)
    produto3 = Produto(3, "Coca-cola", 6.0)
    produto4 = Produto(4, "Energético", 7.0)
    produto5 = Produto(5, "Chocolate", 4.0)

    # Adicionando as instâncias dos produtos na pousada
    pousada.produtos.extend([produto1, produto2,produto3, produto4, produto5])

    # Criando as instâncias das reservas ativas 
    reserva1 = Reserva('Dafni', 1, 3, quarto1, 'A')
    reserva2 = Reserva('Salem', 4, 6, quarto1, 'A')
    reserva3 = Reserva('Luis', 3, 6, quarto3, 'A')
    reserva4 = Reserva('Eduardo', 7, 9, quarto3, 'A')
    reserva5 = Reserva('Maria Luiza', 1, 6, quarto5, 'A')

    # Adicionando as reservas ativas na pousada
    pousada.reservas.extend([reserva1, reserva2, reserva3, reserva4, reserva5])

    # Loop para a repetição do menu
    while True:
    
        print('=========== MENU ===========\n')
        print("1. Consultar Disponibilidade")
        print("2. Consultar Reserva")
        print("3. Realizar Reserva")
        print("4. Cancelar Reserva")
        print("5. Realizar Check-in")
        print("6. Realizar Check-out")
        print("7. Registrar Consumo")
        print("8. Salvar")
        print("0. Sair.\n")

        print('-'* 20)

        # Usuário escolhe uma opção do menu
        opcao = int(input("Escolha uma opção: "))

        # Consulta Disponibilidade 
        if opcao == 1:
            data = int(input("\nInforme o dia que deseja consultar: "))
            quarto_numero = int(input("Informe o número do quarto: "))
            quarto = pousada.quarto[quarto_numero - 1]
            pousada.consulta_disponibilidade(data,quarto)
            
        # Consultar Reserva
        elif opcao == 2:
            print("\nVocê pode consultar pela data, nome do cliente ou o número do quarto. Caso não queria uma opção, somente pule (Enter).\n")
            data_str = str(input("Informe o número do dia que você quer consulta: "))
            cliente = str(input('Digite o nome do cliente: '))
            quarto_numero_str = str(input("Informe o número do quarto: "))
            print('-'*20,"\n")
            
            if data_str:
                data = int(data_str)
            else:
                data = None

            if quarto_numero_str:
                quarto_numero = int(quarto_numero_str) 
            else:
                quarto_numero = None

            if cliente == "":
                cliente = None
            pousada.consulta_reserva(data = data, cliente = cliente, quarto = quarto_numero)
            
        # Realizar Reserva
        elif opcao == 3:
            dia_inicio = int(input('Informe o dia de início: '))
            dia_fim = int(input('Informe o dia final: '))
            cliente = str(input('Informe o seu nome: '))
            quarto_numero = int(input("Informe o número do quarto: "))
            quarto = pousada.quarto[quarto_numero - 1]
            pousada.realiza_reserva(dia_inicio, dia_fim, cliente, quarto)
        
        # Cancelar Reserva
        elif opcao == 4:
            cliente = str(input('Informe o seu nome: '))
            pousada.cancela_reserva(cliente)

        # Realizar Check-In
        elif opcao == 5:
            cliente = str(input('Informe o seu nome: '))
            pousada.realiza_checkin(cliente)

        # Realizar Check-Out
        elif opcao == 6:
            cliente = str(input('Informe o seu nome: '))
            pousada.realiza_checkout(cliente)

        # Registrar Consumo
        elif opcao == 7:
            cliente = str(input('\nInforme o seu nome: '))
            print("")
            pousada.registrar_consumo(cliente)

        # Salvar
        elif opcao == 8:
            pousada.salva_dados()

        # Sair
        elif opcao == 0:
            break

        else:
            print('\nEstá opção não existe. Escolha uma opção válida!')
            
main()