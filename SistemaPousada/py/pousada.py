from reserva import Reserva
from quarto import Quarto
from produto import Produto

# Criando a Classe Pousada
class Pousada:
    # Criando o método construtor para inicializar a classe Pousada
    def __init__ (self, nome:str, contato:str):
        self.nome = nome
        self.contato = contato
        self.quarto = []
        self.reservas = []
        self.produtos = []

    # Criando o método para imprimir as informações da classe Pousada
    def __str__(self):
        return f"Nome: {self.nome} - Contato: {self.contato} - Quartos: {self.quarto} - Reservas: {self.reservas} - Produtos disponiveis: {self.produtos}"
    
    # Método para salvar os dados da Pousada
    def salva_dados(self):
        # Salvando os dados dos quartos
        arquivo_quartos = open("SistemaPousada/SistemaPousada/data/quarto.txt", "w", encoding="UTF-8")
        for quarto in self.quarto:
        # Escreve os dados do quarto no arquivo
            linha_quarto = f"{quarto.numero},{quarto.diaria},{quarto.categoria},{quarto.status}\n"
            arquivo_quartos.write(linha_quarto)
        arquivo_quartos.close()  # Fechar o arquivo manualmente

        # Salvando os dados das reservas
        arquivo_reservas = open("SistemaPousada/SistemaPousada/data/reserva.txt", "w", encoding="UTF-8      ")
        for reserva in self.reservas:
        # Escreve os dados da reserva no arquivo
            linha_reserva = f"{reserva.cliente},{reserva.dia_inicio},{reserva.dia_fim},{reserva.quarto.numero},{reserva.status}\n"
            arquivo_reservas.write(linha_reserva)
        arquivo_reservas.close()  # Fechar o arquivo manualmente

        # Salvando os dados dos produtos
        arquivo_produtos = open("SistemaPousada/SistemaPousada/data/produto.txt", "w", encoding="UTF-8")
        for produto in self.produtos:
        # Escreve os dados do produto no arquivo
           linha_produto = f"{produto.codigo},{produto.nome},{produto.preco}\n"
           arquivo_produtos.write(linha_produto)
        arquivo_produtos.close()  # Fechar o arquivo manualmente

        print("Dados salvos com sucesso.")         

    # Método para carregar os dados da pousada
    def carrega_dados(self):
        # Carregando os dados dos quartos
        arquivo_quartos = open("SistemaPousada/SistemaPousada/data/quarto.txt", "r")
        for linha in arquivo_quartos:
            # Dividir a linha do arquivo em partes e criar o objeto Quarto
            numero, diaria, categoria, status = linha.strip().split(",")
            quarto = Quarto(int(numero), float(diaria), categoria, status)
            self.quarto.append(quarto)  # Adiciona o quarto à lista de quartos
        arquivo_quartos.close()  # Fechar o arquivo manualmente

        # Carregando os dados das reservas
        arquivo_reservas = open("SistemaPousada/SistemaPousada/data/reserva.txt", "r")
        for linha in arquivo_reservas:
            # Dividir a linha do arquivo em partes e criar o objeto Reserva
            cliente, dia_inicio, dia_fim, numero_quarto, status = linha.strip().split(",")
            # Encontrar o quarto correto para a reserva
            quarto_reservado = None
            for quarto in self.quarto:
                if quarto.numero == int(numero_quarto):
                    quarto_reservado = quarto
                    break
            # Se o quarto foi encontrado, cria a reserva
            if quarto_reservado:
                reserva = Reserva(cliente, int(dia_inicio), int(dia_fim), quarto_reservado, status)
                self.reservas.append(reserva)  # Adiciona a reserva à lista de reservas
        arquivo_reservas.close()  # Fechar o arquivo manualmente

        # Carregando os dados dos produtos
        arquivo_produtos = open("SistemaPousada/SistemaPousada/data/produto.txt", "r")
        for linha in arquivo_produtos:
        # Dividir a linha do arquivo em partes e criar o objeto Produto
            codigo, nome, preco = linha.strip().split(",")
            produto = Produto(int(codigo), nome, float(preco))
            self.produtos.append(produto)  # Adiciona o produto à lista de produtos
        arquivo_produtos.close()  # Fechar o arquivo manualmente

        print("Dados carregados com sucesso.")
   
    #  Consulta a disponibilidade dos quartos e se estão disponíveis.
    def consulta_disponibilidade(self, data: int, quarto: Quarto):
    
    # Verificar as reservas para esse quarto
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero:
                if reserva.dia_inicio <= data <= reserva.dia_fim and reserva.status == 'A' or reserva.status == 'I':
                   print(f"\nO quarto {quarto.numero} está ocupado entre os dias {reserva.dia_inicio} e {reserva.dia_fim}.")
                   return False  # Quarto ocupado
        print(f"{quarto} está disponível no dia {data}.")
        return True  # Quarto disponível
    
    # Consulta reservas ativas com base em uma data, nome do cliente e/ou número do quarto.
    def consulta_reserva(self, data: int = None, cliente: str = None, quarto: Quarto = None):
        # Cria lista para armazenar as reservas encontradas
        reservas_encontradas = []
        
        # Verifica o status da reserva 
        for reserva in self.reservas:
            if reserva.status == 'A':
                pass

            # Criando variáveis para consultar as reservas
            data_encontrada = (data is None or (reserva.dia_inicio <= data <= reserva.dia_fim))
            cliente_encontrado = (cliente is None or reserva.cliente == cliente)
            quarto_encontrado = (quarto is None or reserva.quarto.numero == quarto)

            # Se a reserva existe, ela é adicionada a lista "reservas_encontradas"
            if data_encontrada and cliente_encontrado and quarto_encontrado:
                reservas_encontradas.append(reserva)

        # Imprimindo as reservas encontradas na tela
        if reservas_encontradas:
            for reserva in reservas_encontradas:
                print(f"========== Reserva(s) encontrada(s) ========== \n\nCliente: {reserva.cliente}\nQuarto: {reserva.quarto.numero}\nDia Inicio: {reserva.dia_inicio}\nDia Final: {reserva.dia_fim}\nCategora: {reserva.quarto.categoria}\nStatus: {reserva.status}\nDiária: {reserva.quarto.diaria}\n")
                      
        else:
            print(f"Nenhuma reserva encontrada com essas informações.")          

    # Faz uma reserva para o cliente se o quarto estiver disponível e o cliente não tiver outra reserva ativa.
    def realiza_reserva(self, data_inicio: int, data_fim: int, cliente: str, quarto: Quarto):

        # Verifica se o quarto está ocupado no período solicitado
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero and reserva.status == 'A' or reserva.status == 'I':
                # Verifica se as datas da nova reserva estão dentro de uma reserva existente
                if data_inicio <= reserva.dia_fim and data_fim >= reserva.dia_inicio:
                    print(f"Quarto {quarto.numero} está ocupado entre os dias {reserva.dia_inicio} e {reserva.dia_fim}.")
                    return False  # Quarto ocupado

        # Verifica se o cliente já tem uma reserva ativa
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A' or reserva.status == 'T' :
                print(f"Cliente {cliente} já tem uma reserva ativa na pousada.")
                return False  # Cliente já tem reserva ativa

        # Se o quarto estiver disponível e o cliente não tiver outra reserva, cria uma nova reserva
        nova_reserva = Reserva(cliente, data_inicio, data_fim, quarto, 'A')  # Status 'A' para Ativa
        self.reservas.append(nova_reserva)
        print(f"Reserva realizada com sucesso para o(a) cliente {cliente}.")
        return True

    # Cancela a reserva ativa de um cliente.
    def cancela_reserva(self, cliente):

        # Verifica se o cliente tem uma reserva ativa e cancela
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva.status = 'C'
                print(f"Reserva cancelada com sucesso.")
                return True
            
        print(f"Não foi encontrada uma reserva ativa para o(a) cliente {cliente}.")
        return False

    # Realiza o check-in do cliente se ele tiver uma reserva ativa.
    def realiza_checkin(self, cliente: str):
        
        for reserva in self.reservas:
            #Calcula o período de dias e o valor total da diária
            dia_total = reserva.dia_fim - reserva.dia_inicio
            diaria_total = reserva.quarto.diaria * dia_total

            # Verifica se o cliente informado tem uma reserva ativa e realiza o check-in
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva.status = 'I'  # Muda o status para Check-In
                print(f"\n{cliente} realizou o check-in no quarto {reserva.quarto.numero}, entre os dias {reserva.dia_inicio} e {reserva.dia_fim}, pelo período de {dia_total} dias.\nNo valor total de R${diaria_total}.\n")
                return True

        print(f"Não foi encontrada nenhuma reserva ativa para o cliente {cliente}.")
        return False
    
    # Realiza o check-out do cliente, finalizando a estadia e limpando o consumo.
    def realiza_checkout(self, cliente: str):
        
        for reserva in self.reservas:
            # Verifica se o cliente tem um check-in ativo
            if reserva.cliente == cliente and reserva.status == 'I':
                # Calcula valor total da diaria e do consumo e o periodo de dias 
                total_consumo = reserva.quarto.valor_total_consumo()
                dias = reserva.dia_fim - reserva.dia_inicio
                total_diaria = dias * reserva.quarto.diaria
                valor_total = total_consumo + total_diaria
                
                #Imprime as informações do check-out na tela
                print(f"\n{cliente} realizou o check-out do quarto {reserva.quarto.numero}. No qual se hospedou entre os dias {reserva.dia_inicio} e {reserva.dia_fim}, no período de {dias} dias. \nNo valor total da diária: R${total_diaria:.2f}\n")
                print('-'*15,'Produtos Consumidos','-'*15,'\n')
                reserva.quarto.lista_consumo()
                print('-'*50)
                print(f"Valor total consumido: {total_consumo}")
                print(f"Valor total á ser pago: {valor_total}\n")

                #Muda o Status e limpa o consumo
                reserva.status = 'O'
                reserva.quarto.limpa_consumo()
                return True
            
        print(f"Não foi encontrado check-in ativo para o(a) cliente {cliente}.")
        return False
    
    # Método para registro de consumo dos produtos
    def registrar_consumo(self, cliente: str):
        for reserva in self.reservas:
            # Verifica se o cliente tem um check-in ativo no nome dele
            if reserva.cliente == cliente and reserva.status == "I": 
                # Repete o menu dos produto da pousada
                while True:
                    print('='*20,'Copa','='*20,'\n')
                    for produto in self.produtos:
                        print(produto)
                    print('-'*46)

                    # Usuário escolhe o código de um produto
                    opcao = int(input('\nEscolha o código do produto: '))

                    # Verifica a existência do produto selecionado pelo cliente
                    produto_selecionado = None
                    for produto in self.produtos:
                        if opcao == produto.codigo:
                            produto_selecionado = produto
                            break
            
                    # Adiciona o produto selecionado ao consumo do quarto e imprime a lista de consumo
                    if produto_selecionado:
                        reserva.quarto.adiciona_consumo(produto_selecionado)
                        print(f"\nProduto {produto_selecionado.nome} adicionado ao consumo.")
                        print('-'*46)
                        reserva.quarto.lista_consumo()
                        print('')
                    else:
                        print('\nEste código de produto não existe. Insira um valor válido.')

                    # Pergunta ao usuário se ele deseja continuar consumindo
                    mais_produto = str(input('\nVocê deseja mais algum produto?(S/N) '))
                    print('')
                    if mais_produto == 's' or mais_produto == 'S':
                        continue
                    else:
                        return False
        else: 
            print(f'Não existe check-in para o(a) cliente {cliente}.')