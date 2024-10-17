from pousada import Pousada
from quarto import Quarto
from reserva import Reserva
from produto import Produto

# Criando o método main para reproduzir o menu
def main():

    # Criando a instância pousada
    pousada = Pousada('Pousada Salem e Pesca', '@salemepesca')

    # Carregar todos os dados (quartos, reservas, produtos) da pousada
    pousada.carrega_dados()

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