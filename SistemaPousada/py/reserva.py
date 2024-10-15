from quarto import Quarto

# Criando a Classe Reserva
class Reserva:

    # Criando o método construtor para inicializar a classe Reserva                       
    def __init__(self, cliente:str, dia_inicio:int, dia_fim:int, quarto: Quarto, status='A'):
        self.cliente = cliente
        self.quarto = quarto
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.status = status  # A: Ativa, C: Cancelada, I: Check-In, O: Check-Out
    
    # Criando o método para imprimir as informações da classe Reserva
    def __str__(self):
        return f"Reserva de {self.cliente} no quarto {self.quarto.numero}, de {self.dia_inicio} a {self.dia_fim}. Status: {self.status}"