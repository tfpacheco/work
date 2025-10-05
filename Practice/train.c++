#include <iostream>
using namespace std;

struct livros {
    string titulo;
    string autor;
    int ano;
};

void mostrarLivro(livros a) {
    cout << "Titulo: " << a.titulo << endl;
    cout << "Autor: " << a.autor << endl;
    cout << "Ano: " << a.ano << endl;
}

int main() {
    livros b;

    cout << "Digite o titulo do livro: ";
    getline(cin, b.titulo);

    cout << "Digite o autor do livro: ";
    getline(cin, b.autor);

    cout << "Digite o ano do livro: ";
    cin >> b.ano;

    cout << "\n--- Dados do Livro ---\n";
    mostrarLivro(b);

    return 0;
}
