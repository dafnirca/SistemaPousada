from reserva import Reserva
from quarto import Quarto
from produto import Produto

class Pousada:
    # Criando o método init para inicializar a classe 
    def __init__ (self, nome:str, contato:str):
        self.nome = nome
        self.contato = contato
        self.quarto = []
        self.reservas = []
        self.produtos = []

    
    def salva_dados(self):
    # Salvando os dados dos quartos
        arquivo_quartos = open("data/quarto.txt", "w")
        for quarto in self.quarto:
        # Escreve os dados do quarto no arquivo
            linha_quarto = f"{quarto.numero},{quarto.diaria},{quarto.categoria},{quarto.status}\n"
            arquivo_quartos.write(linha_quarto)
        arquivo_quartos.close()  # Fechar o arquivo manualmente

    # Salvando os dados das reservas
        arquivo_reservas = open("data/reserva.txt", "w")
        for reserva in self.reservas:
        # Escreve os dados da reserva no arquivo
            linha_reserva = f"{reserva.cliente},{reserva.dia_inicio},{reserva.dia_fim},{reserva.quarto.numero},{reserva.status}\n"
            arquivo_reservas.write(linha_reserva)
        arquivo_reservas.close()  # Fechar o arquivo manualmente

    # Salvando os dados dos produtos
        arquivo_produtos = open("data/produto.txt", "w")
        for produto in self.produtos:
        # Escreve os dados do produto no arquivo
           linha_produto = f"{produto.codigo},{produto.nome},{produto.preco}\n"
           arquivo_produtos.write(linha_produto)
        arquivo_produtos.close()  # Fechar o arquivo manualmente

        print("Dados salvos com sucesso.")         

    def carrega_dados(self):
    # Carregando os dados dos quartos
        arquivo_quartos = open("data/quarto.txt", "r")
        for linha in arquivo_quartos:
        # Dividir a linha do arquivo em partes e criar o objeto Quarto
            numero, diaria, categoria, status = linha.strip().split(",")
            quarto = Quarto(int(numero), float(diaria), categoria, status)
            self.quarto.append(quarto)  # Adiciona o quarto à lista de quartos
        arquivo_quartos.close()  # Fechar o arquivo manualmente

    # Carregando os dados das reservas
        arquivo_reservas = open("data/reserva.txt", "r")
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
        arquivo_produtos = open("data/produto.txt", "r")
        for linha in arquivo_produtos:
        # Dividir a linha do arquivo em partes e criar o objeto Produto
            codigo, nome, preco = linha.strip().split(",")
            produto = Produto(int(codigo), nome, float(preco))
            self.produtos.append(produto)  # Adiciona o produto à lista de produtos
        arquivo_produtos.close()  # Fechar o arquivo manualmente

        print("Dados carregados com sucesso.")
   
    def consulta_disponibilidade(self, data: int, quarto: Quarto):
    #  Consulta a disponibilidade dos quartos e se estão disponíveis.
    # Verificar as reservas para esse quarto
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero:
                if reserva.dia_inicio <= data <= reserva.dia_fim and reserva.status == 'A':
                   print(f"Quarto {quarto.numero} está ocupado de {reserva.dia_inicio} a {reserva.dia_fim}.")
                   return False  # Quarto ocupado
        print(f"Quarto {quarto.numero} está disponível na data {data}.")
        return True  # Quarto disponível

    def consulta_reserva(self, data: int = None, cliente: str = None, quarto: Quarto = None):
      # Consulta reservas ativas com base em uma data, nome do cliente e/ou número do quarto.
        for reserva in self.reservas:
            if (cliente and reserva.cliente == cliente) or (quarto and reserva.quarto.numero == quarto.numero) or (data and reserva.dia_inicio <= data <= reserva.dia_fim):
               print(f"Reserva encontrada: Cliente: {reserva.cliente}, Quarto: {reserva.quarto.numero}, de {reserva.dia_inicio} a {reserva.dia_fim}. Status: {reserva.status}")
               return reserva
        print("Nenhuma reserva encontrada.")
        return None

    def realiza_reserva(self, data_inicio: int, data_fim: int, cliente: str, quarto: Quarto):
      # Faz uma reserva para o cliente se o quarto estiver disponível e o cliente não tiver outra reserva ativa.

    # Verifica se o quarto está ocupado no período solicitado
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero and reserva.status == 'A':
            # Verifica se as datas da nova reserva estão dentro de uma reserva existente
                if data_inicio <= reserva.dia_fim and data_fim >= reserva.dia_inicio:
                    print(f"Quarto {quarto.numero} está ocupado de {reserva.dia_inicio} a {reserva.dia_fim}.")
                    return False  # Quarto ocupado

    # Verifica se o cliente já tem uma reserva ativa
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                print(f"Cliente {cliente} já tem uma reserva ativa.")
                return False  # Cliente já tem reserva ativa

    # Se o quarto estiver disponível e o cliente não tiver outra reserva, cria uma nova reserva
        nova_reserva = Reserva(cliente, data_inicio, data_fim, quarto, 'A')  # Status 'A' para Ativa
        self.reservas.append(nova_reserva)
        print(f"Reserva realizada com sucesso para o cliente {cliente}.")
        return True

    def cancela_reserva(self, cliente):
        # Cancela a reserva ativa de um cliente.
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva.status = 'C'
                print(f"Reserva de {cliente} foi cancelada com sucesso.")
                return True
            
        print(f"Não foi encontrada uma reserva ativa para o cliente {cliente}.")
        return False

    def realiza_checkin(self, cliente: str):
        #  Realiza o check-in do cliente se ele tiver uma reserva ativa.

        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva.status = 'I'  # Muda o status para Check-In
                print(f"Check-in realizado para o cliente {cliente}. Quarto {reserva.quarto.numero}, de {reserva.dia_inicio} a {reserva.dia_fim}.")
                return True

        print(f"Não foi encontrada uma reserva ativa para o cliente {cliente}.")
        return False

    def realiza_checkout(self, cliente: str):
        # Realiza o check-out do cliente, finalizando a estadia e limpando o consumo.

        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'I':
                dias = reserva.dia_fim - reserva.dia_inicio
                valor_total = dias * reserva.quarto.diaria + reserva.quarto.valor_total_consumo()
                print(f"Check-out realizado para o cliente {cliente}. Valor final: R${valor_total:.2f}")
                reserva.status = 'O'
                reserva.quarto.limpa_consumo()
                return True
            
        print(f"Não foi encontrado check-in ativo para o cliente {cliente}.")
        return False
        
def main():

    # Criando a pousada
    pousada = Pousada('Pousada Salem e Pesca', '@salemepesca')

    # Criando alguns quartos, produtos e reservas
    quarto1 = Quarto(1, 100.0, 'S', 'L')
    quarto2 = Quarto(2, 200.0, 'M', 'L')
    quarto3 = Quarto(3, 300.0, 'P', 'L')
    pousada.quarto.extend([quarto1, quarto2, quarto3])

    produto1 = Produto(1, "Café", 5.0)
    produto2 = Produto(2, "Água", 2.0)
    pousada.produtos.extend([produto1, produto2])

    reserva1 = Reserva('Cliente A', 1, 3, quarto1, 'A')
    pousada.reservas.append(reserva1)

    pousada.quarto.append(quarto1)
    pousada.quarto.append(quarto2)
    pousada.produtos.append(produto1)
    pousada.reservas.append(reserva1)

    # Salvando os dados
    pousada.salva_dados()

    # Limpando as listas para testar o carregamento
    pousada.quarto.clear()
    pousada.reservas.clear()
    pousada.produtos.clear()

    # Carregando os dados novamente
    pousada.carrega_dados()

    # Teste das funções
    print("\n--- Teste de disponibilidade ---")
    pousada.consulta_disponibilidade(2, quarto1)  # Deve retornar ocupado
    pousada.consulta_disponibilidade(4, quarto1)  # Deve retornar disponível
    
    print("\n--- Teste de consulta de reserva ---")
    pousada.consulta_reserva(2, 'Cliente A', quarto1)

    print("\n--- Teste de realização de reservas ---")
    pousada.realiza_reserva(4, 6, 'Cliente A', quarto1)  # Deve falhar, pois Cliente A já tem reserva ativa
    pousada.realiza_reserva(4, 6, 'Cliente B', quarto2)  # Deve ser bem-sucedido

    print("\n--- Teste de cancelamento de reserva ---")
    pousada.cancela_reserva('Cliente B')  # Cancela a reserva de Cliente B

    print("\n--- Teste de check-in ---")
    pousada.realiza_checkin('Cliente A')  # Realiza o check-in de Cliente A
    
    print("\n--- Teste de check-out ---")
    pousada.realiza_checkout('Cliente A')  # Realiza o check-out de Cliente A

main()
