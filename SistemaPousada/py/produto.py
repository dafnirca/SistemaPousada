class Produto:

    def __init__(self, codigo:int, nome:str, preco:float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        # Define como o produto será representado quando impresso
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: R$ {self.preco:.2f}"