#include <iostream>
using namespace std;

struct Artista{
    string nome;
    string nacionalidade;
};

struct Album{
    string titulo;
    int ano;
    string genero;
    Artista artista;
};


int main(){

    Artista artista1;
    artista1.nome = "Eminem";
    artista1.nacionalidade = "Americano";

    Album album1;
    album1.titulo = "Recovery";
    album1.ano = 2010;
    album1.genero = "Hip-Hop";
    album1.artista = artista1;


}