from reserva import Reserva
from quarto import Quarto
from produto import Produto

class Pousada:
    # Criando o método init para inicializar a classe 
    def __init__ (self, nome:str, contato:str, quartos: Quarto, reservas: Reserva, produtos: Produto ):
        self.nome = nome
        self.contato = contato
        self.quartos = quartos
        self.reservas = reservas
        self.produtos = produtos

    def carrega_dados():


    def salva_dados():

    #Definir a 'data' no menu
    def consulta_disponibilidade(self,data, quarto):
        """Verifica se a data está dentro do período da reserva e se a reserva está ativa."""
        return self.dia_inicio <= data <= self.dia_fim and self.status == 'A'
    
    def consulta_reserva(self, data, cliente, quarto):


    def realiza_reserva(self, data, cliente, quarto):


    def cancela_reserva(self, cliente):


    def realiza_checkin(self, cliente):

    def realiza_checkout(self,cliente):


