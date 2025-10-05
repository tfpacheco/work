#include <iostream>
using namespace std;

void alunos(string nome, int idade, float nota1, float nota2, float nota3){
    cout << "Nome: " << nome << endl;
    cin >> nome;
    cout << "Idade: " << idade << endl;
    cin >> idade;       
    cout << "Nota 1: " << nota1 << endl;
    cin >> nota1;
    cout << "Nota 2: " << nota2 << endl;
    cin >> nota2;
    cout << "Nota 3: " << nota3 << endl;
    cin >> nota3;
}

float media(float nota1, float nota2, float nota3){
    return (nota1 + nota2 + nota3) / 3;
}   

int main(){
    string nome;
     int idade;
      float nota1;
       float nota2;
        float nota3;
         float m = media(nota1, nota2, nota3) / 3;

    cout << "Nome: ";
    cin >> nome;
    cout << "Idade: ";
    cin >> idade;       
    cout << "Nota 1: ";
    cin >> nota1;
    cout << "Nota 2: ";
    cin >> nota2;
    cout << "Nota 3: ";
    cin >> nota3;

    if(m >= 9,5){
        cout << "O aluno foi aprovado "<< endl;
    }else if(m >= 7,0 && m < 9,5){
        cout << "O aluno foi para recuperacao"  << endl;
}else if(m < 7,0){
    cout << "O aluno foi reprovado"  << endl;
}
}