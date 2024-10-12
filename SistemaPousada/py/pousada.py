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

        arquivo_quartos = open("SistemaPousada/SistemaPousada/data/quarto.txt", "w")
        for quarto in self.quarto:
                arquivo_quartos.write(f"{quarto.numero},{quarto.diaria},{quarto.categoria},{quarto.status},{quarto.codigo}\n")
        arquivo_quartos.close()

        arquivo_reservas = open("SistemaPousada/SistemaPousada/data/reserva.txt", "w")
        for reserva in self.reservas:
                arquivo_reservas.write(f"{reserva.cliente},{reserva.dia_inicio},{reserva.dia_fim},{reserva.quarto}\n")
        arquivo_reservas.close()

        arquivo_produtos = open("SistemaPousada/SistemaPousada/data/produto.txt", "w")
        for produto in self.produtos:
                arquivo_produtos.write(f"{produto.codigo},{produto.nome},{produto.preco}\n")
        arquivo_produtos.close()
            

    def carrega_dados(self):
          
        arquivo_quartos = open("SistemaPousada/SistemaPousada/data/quarto.txt", "r")
        quartos = arquivo_quartos.read()
        print( '=' * 10 + " Quartos " + '=' * 10)
        print(f"Número:{quartos[0]} ")
        print(f"Valor da diaria:{quartos[1]} ")
        print(f"Categoria:{quartos[2]} ")           #Criar a tabela das informações
        print(f"Status:{quartos[3]} ")
        
        arquivo_quartos.close()

        arquivo_reservas= open("SistemaPousada/SistemaPousada/data/reserva.txt", "r")
        reserva = arquivo_reservas.read()
        print('=' * 10 + " Reservas " + '=' * 10)
        print(f"Número:{reserva[0]} ")
        print(f"Valor da diaria:{reserva[1]} ")     #Criar a tabela das informações
        print(f"Categoria:{reserva[2]} ")
        print(f"Status:{reserva[3]} ")
        arquivo_reservas.close()
        
        arquivo_produtos = open("SistemaPousada/SistemaPousada/data/produto.txt", "r")
        produtos = arquivo_produtos.read()
        print(produtos)                             #Criar a tabela das informações
        arquivo_produtos.close()

    #consultando a disponibilidade dos quartos e se estão disponíveis.
    def consulta_disponibilidade(self, data: int, quarto: Quarto):
    # Verificar as reservas para esse quarto
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero:
                if reserva.dia_inicio <= data <= reserva.dia_fim and reserva.status == 'A':
                   print(f"Quarto {quarto.numero} está ocupado de {reserva.dia_inicio} a {reserva.dia_fim}.")
                   return False  # Quarto ocupado
        print(f"Quarto {quarto.numero} está disponível na data {data}.")
        return True  # Quarto disponível

    def consulta_reserva(self, data: int, cliente: str, quarto: Quarto):
        for reserva in self.reservas:
            if (cliente and reserva.cliente == cliente) or (quarto and reserva.quarto.numero == quarto.numero) or (data and reserva.dia_inicio <= data <= reserva.dia_fim):
               print(f"Reserva encontrada: Cliente: {reserva.cliente}, Quarto: {reserva.quarto.numero}, de {reserva.dia_inicio} a {reserva.dia_fim}. Status: {reserva.status}")
               return reserva
        print("Nenhuma reserva encontrada.")

        
def main():
    # Criando a pousada
    pousada = Pousada('Pousada Salem e Pesca', '@salemepesca')
    
    # Criando quartos
    quarto1 = Quarto(1, 100.0, 'S', 'L')
    quarto2 = Quarto(2, 200.0, 'M', 'L')
    quarto3 = Quarto(3, 300.0, 'P', 'L')
    pousada.quarto.extend([quarto1, quarto2, quarto3])  # Adicionando os quartos à lista

    # Criando produtos
    produto1 = Produto(1, "Café", 5.0)
    produto2 = Produto(2, "Água", 2.0)
    pousada.produtos.extend([produto1, produto2])

    # Criando reservas
    reserva1 = Reserva('Cliente A', 1, 3, quarto1, 'A')
    pousada.reservas.append(reserva1)
    
    # Teste das funções
    print("Testes:")
    pousada.consulta_disponibilidade(2, quarto1)  # Deve retornar ocupado
    pousada.consulta_disponibilidade(4, quarto1)  # Deve retornar disponível
    
    pousada.consulta_reserva(2, 'Cliente A', quarto1)

main()