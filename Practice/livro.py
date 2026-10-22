class Livro:

    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro: {self.titulo} foi emprestado")
        else:
            print(f"O livro: {self.titulo} não foi emprestado")

    def devolver(self):
            if not self.disponivel:
                self.disponivel = True
                print('Livro devolvido com sucesso.')
            else:
                print('O livro já está disponível.')
    
    def descrever(self):
            print('Título:', self.titulo)
            print('Autor:', self.autor)
    
            if self.disponivel:
                print('Disponibilidade: Disponível')
            else:
                print('Disponibilidade: Emprestado')
