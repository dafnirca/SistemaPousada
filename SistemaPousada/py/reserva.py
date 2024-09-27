from quarto import Quarto
class Reserva:
    # Criando o método init para inicializar a classe                           #Verificar com a sora
    def __init__(self, cliente:str, quarto:Quarto, dia_inicio:int, dia_fim:int, status=['A','C','I','O']):
        self.cliente = cliente
        self.quarto = quarto
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.status = status  # A: Ativa, C: Cancelada, I: Check-In, O: Check-Out
    
    # Criando o método para imprimir as informações da classe Reserva
    def __str__(self):
        return f"Reserva de {self.cliente} no quarto {self.quarto}, de {self.dia_inicio} a {self.dia_fim}. Status: {self.status}"
