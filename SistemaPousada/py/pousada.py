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

        numero_quarto = quarto.get('numero')

        if not numero_quarto:
            print("Número do quarto não foi encontrado.")
            return False
             
    # # Procurar o quarto na lista de quartos
    #     quarto_encontrado = False
    #     for i in self.quarto: 
    #         if i == self.numero:
    #             quarto_encontrado = True
    #         break

    #     if not quarto_encontrado:
    #         print(f"Quarto {quarto} não encontrado.")
    #         return False   
        
        # Verificar as reservas para esse quarto
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto.numero:
                # Se a data fornecida está no intervalo da reserva, o quarto está ocupado
                if reserva.dia_inicio <= data <= reserva.dia_fim and reserva.status == 'A':
                    print(f"Quarto {quarto.numero} está ocupado de {reserva.dia_inicio} a {reserva.dia_fim}.")
                    return False  # Quarto ocupado
        
        print(f"Quarto {quarto.numero} está disponível na data {data}.")
        return True  # Quarto disponível    
        


            
        
def main():

    i = Pousada('Pousada Salem e Pesca', '@salemepesca')

    i.quarto.append(Quarto(1,1000,'S','L',1))
    i.reservas.append(Reserva('Dafni',1 , 4, 1,'A'))
    i.produtos.append(Produto(1, 'Café', 10))

    i.salva_dados()
    i.carrega_dados()
    
    i.consulta_disponibilidade(1,1)
    
    

main()