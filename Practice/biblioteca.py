class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def listar_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:
                livro.descrever()

    def procurar(self, autor):
        encontrou = False

        for livro in self.livros:
            if livro.autor == autor:
                livro.descrever()
                encontrou = True

        if not encontrou:
            print('Não foram encontrados livros desse autor.')
