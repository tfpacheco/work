/*
#include <iostream>
using namespace std;

struct Pessoa{
    string nome;
    int idade;
    float altura;
};

void mostrarPessoa(Pessoa p){
cout << p.nome << endl;
cout << p.idade << endl;
cout << p.altura << endl;
}

int main(){

Pessoa p1;
p1 = {"joao", 16, 1.75};
mostrarPessoa(p1);
}
*/

/*#include <iostream>
using namespace std;

struct Aluno{
    string nome;
    float nota1;
    float nota2;
    float nota3;
};


float calcularMedia(Aluno a){
    return (a.nota1 + a.nota2 + a.nota3) / 3;
}

int main(){

    Aluno a1 = {"Martim", 10.5, 6.6, 8.9};
    cout << calcularMedia(a1);

    
}
    */


#include <iostream>
using namespace std;

struct Produto{
    string nome;
    float preco;
    int quantidade;
};

void mostrarProduto(Produto p){
    cout << p.nome << endl;
    cout << p.preco << endl;
    cout << p.quantidade << endl;
}

float valorTotalEstoque(Produto p){
    float valorTotal = p.preco * p.quantidade;
    return valorTotal;
};

int main(){
Produto p1 = {"Borracha", 2.50, 3};
Produto p2 = {"Lapis", 1.50, 2};
Produto p3 = {"Caneta", 4.20, 2};
mostrarProduto(p1);
cout << valorTotalEstoque(p1);
}

