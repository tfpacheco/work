def livro_favorito(titulo):
    print(f"Um dos meus livros favoritos é {titulo}")

livro_favorito("os Maias")

def mostrar_mensagem():
    print("Funções")

mostrar_mensagem()


def fazer_tshirt(tamanho, mensagem):
    print(f"O tamanho é {tamanho} e a mensagem é {mensagem}")

fazer_tshirt(tamanho="M", mensagem="Olá es um uneca")

def criar_album(artista, titulo, faixas=None):
    pessoa = {'artista': artista, 'titulo': titulo}
    print(f"Artista: {artista}, Título: {titulo}, Faixas: {faixas}")
    if faixas is not None:
        pessoa['faixas'] = faixas
    return pessoa

album1 = criar_album("The Beatles", "Abbey Road")
album2 = criar_album("Pink Floyd", "The Dark Side of the Moon", faixas=10)
album3 = criar_album("Eminem", "Recovery")
