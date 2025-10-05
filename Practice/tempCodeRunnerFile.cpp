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