# Criando a classe Produto
class Produto:

    #Inicializando o método construtor para inicializar a classe Produto
    def __init__(self, codigo:int, nome:str, preco:float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

     # Define como o produto será representado quando impresso
    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: R$ {self.preco:.2f}"