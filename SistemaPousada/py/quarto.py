from produto import Produto

class Quarto:
     # Verificar sobre o valor do atributo 'categoria' (char)
     # Criando o método init para inicializar a classe
    def __init__(self, numero:int, diaria:float, categoria=['S','M','P'], status=['L','O'], codigo = Produto):
        self.numero = numero
        self.categoria = categoria  # S: Standard, M: Master, P: Premium
        self.diaria = diaria        # Valor da diária do quarto
        self.status = status        # L: Livre, O: Ocupado
        self.consumo = []           # Lista de códigos de produtos consumidos
        self.codigo = codigo
    
    def adiciona_consumo(self, produto):
        """Adiciona um produto à lista de consumo."""
        self.consumo.append(produto)
        print(self.consumo)
    
    def lista_consumo(self):
        for item in self.consumo:
            print(item)
    
    def valor_total_consumo(self):
        total = 0
        for produto in self.consumo:
            total += produto.preco
        return total
        

    def limpa_consumo(self):
        """Limpa o consumo após o check-out."""
        self.consumo.clear()

    # Criando o método para imprimir as informações da classe Quarto
    def __str__(self):
        return f"Quarto {self.numero} - Categoria: {self.categoria}, Status: {self.status}, Diária: R$ {self.diaria:.2f}"

def main():
     
    produto1 = Produto(1, "Café", 5.00)
    produto2 = Produto(2, "Chá", 4.00)
    produto3 = Produto(3,"Água", 2.00)

    quarto1 = Quarto(1,1.000 ,"S", "L")

    quarto1.adiciona_consumo(produto1)
    quarto1.adiciona_consumo(produto2)
    quarto1.adiciona_consumo(produto3)

    print("\nProdutos consumidos:")
    quarto1.lista_consumo()


    total = quarto1.valor_total_consumo()
    print(f"Valor total consumo:{total}")

    """j = Produto(1, "Café", 5.00)
       i = Quarto
       i.adiciona_consumo(j) """

main()
