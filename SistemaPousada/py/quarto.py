class Quarto:
    def __init__(self, numero, categoria, diaria, status='L'):
        self.numero = numero
        self.categoria = categoria  # S: Standard, M: Master, P: Premium
        self.diaria = diaria        # Valor da diária do quarto
        self.status = status        # L: Livre, O: Ocupado
        self.consumo = []           # Lista de códigos de produtos consumidos
    
    def registrar_consumo(self, codigo_produto):
        """Adiciona um produto à lista de consumo."""
        self.consumo.append(codigo_produto)
    
    def limpar_consumo(self):
        """Limpa o consumo após o check-out."""
        self.consumo.clear()
    
    def __str__(self):
        return f"Quarto {self.numero} - Categoria: {self.categoria}, Status: {self.status}, Diária: R$ {self.diaria:.2f}"
