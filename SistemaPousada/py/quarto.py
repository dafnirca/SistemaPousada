from produto import Produto

# Criando a Classe Quarto
class Quarto:
    
     # Criando o método construtor para inicializar a classe Quarto
    def __init__(self, numero:int, diaria:float, categoria=['S'], status=['L'], codigo = Produto):
        self.numero = numero
        self.categoria = categoria  # S: Standard, M: Master, P: Premium
        self.diaria = diaria        # Valor da diária do quarto
        self.status = status        # L: Livre, O: Ocupado
        self.consumo = []           # Lista de códigos de produtos consumidos
        self.codigo = codigo
    

    # Criando o método para imprimir as informações da classe Quarto
    def __str__(self):
        return f"Quarto {self.numero} - Categoria: {self.categoria}, Status: {self.status}, Diária: R$ {self.diaria:.2f}"
    
    # Adiciona um produto à lista de consumo.
    def adiciona_consumo(self, codigo):
        self.consumo.extend([codigo]) 

    # Lista produtos consumidos pelo quarto.
    def lista_consumo(self):
        for item in self.consumo:
            print(item)

    # Calcula o valor total do consumo
    def valor_total_consumo(self):
        total = 0
        for produto in self.consumo:
            total += produto.preco
        return total
        
    # Limpa o consumo após o check-out.
    def limpa_consumo(self):
        self.consumo.clear()
        return