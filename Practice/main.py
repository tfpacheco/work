from livro import Livro
from biblioteca import Biblioteca
from menu import mostrar_menu


biblioteca = Biblioteca()

livro1 = Livro('Os maias', 'Eça de Queirós')
livro2 = Livro('e isse e nao passa disse', 'Fernando Person')
livro3 = Livro('As aventuras do xavi palito', 'drogado de santo antonio')
livro4 = Livro('Ahh', 'Eça de Queirós')
livro5 = Livro('O meu mais mocim', 'Minha pedra preciosa')

biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.adicionar(livro3)
biblioteca.adicionar(livro4)
biblioteca.adicionar(livro5)

ativo = True
while ativo:    
    opcao == mostrar_menu()

    if opcao =='1':
         

    elif opcao == '5':
          ativo = False

