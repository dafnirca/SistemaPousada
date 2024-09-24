class Reserva:
    def __init__(self, nome_cliente, numero_quarto, data_inicial, data_final, status='A'):
        self.nome_cliente = nome_cliente
        self.numero_quarto = numero_quarto
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.status = status  # A: Ativa, C: Cancelada, I: Check-In, O: Check-Out
    
    def verificar_disponibilidade(self, data):
        """Verifica se a data está dentro do período da reserva e se a reserva está ativa."""
        return self.data_inicial <= data <= self.data_final and self.status == 'A'
    
    def __str__(self):
        return f"Reserva de {self.nome_cliente} no quarto {self.numero_quarto}, de {self.data_inicial} a {self.data_final}. Status: {self.status}"
