#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int LINHA = 5;
const int COLUNA = 5;
const int MAX_NUM = 75;

struct Cartao {
    int numeros[LINHA][COLUNA];
    bool marcados[LINHA][COLUNA];
};

void embaralhar(int arr[], int tamanho) {
    for (int i = tamanho - 1; i > 0; --i) {
        int j = rand() % (i + 1);
        swap(arr[i], arr[j]);
    }
}

void gerarCartao(Cartao &c) {
    int numeros[MAX_NUM];
    for (int i = 0; i < MAX_NUM; ++i)
        numeros[i] = i + 1;

    embaralhar(numeros, MAX_NUM);

    int idx = 0;
    for (int i = 0; i < LINHA; ++i) {
        for (int j = 0; j < COLUNA; ++j) {
            c.numeros[i][j] = numeros[idx++];
            c.marcados[i][j] = false;
        }
    }

    // Casa central grátis
    c.numeros[2][2] = 0;
    c.marcados[2][2] = true;
}

void mostrarCartao(const Cartao &c) {
    cout << "Seu Cartão de Bingo:" << endl;
    for (int i = 0; i < LINHA; ++i) {
        for (int j = 0; j < COLUNA; ++j) {
            if (c.numeros[i][j] == 0) {
                cout << "FREE\t";
            } else if (c.marcados[i][j]) {
                cout << "\033[31m[" << c.numeros[i][j] << "]\033[0m\t";
            } else {
                cout << c.numeros[i][j] << "\t";
            }
        }
        cout << endl;
    }
    cout << endl;
}


bool verificarVitoria(const Cartao &c) {
    // Linhas
    for (int i = 0; i < LINHA; ++i) {
        bool completa = true;
        for (int j = 0; j < COLUNA; ++j) {
            if (!c.marcados[i][j]) {
                completa = false;
                break;
            }
        }
        if (completa) return true;
    }

    // Colunas
    for (int j = 0; j < COLUNA; ++j) {
        bool completa = true;
        for (int i = 0; i < LINHA; ++i) {
            if (!c.marcados[i][j]) {
                completa = false;
                break;
            }
        }
        if (completa) return true;
    }

    // Diagonal principal
    bool diag1 = true;
    for (int i = 0; i < LINHA; ++i) {
        if (!c.marcados[i][i]) {
            diag1 = false;
            break;
        }
    }
    if (diag1) return true;

    // Diagonal secundária
    bool diag2 = true;
    for (int i = 0; i < LINHA; ++i) {
        if (!c.marcados[i][COLUNA - 1 - i]) {
            diag2 = false;
            break;
        }
    }
    if (diag2) return true;

    return false;
}

void marcarNumero(Cartao &c, int num) {
    for (int i = 0; i < LINHA; ++i) {
        for (int j = 0; j < COLUNA; ++j) {
            if (c.numeros[i][j] == num) {
                c.marcados[i][j] = true;
                cout << "Número " << num << " marcado na posição (" << i << "," << j << ")!" << endl;
                return;
            }
        }
    }
    cout << "Número " << num << " não está no seu cartão." << endl;
}

int main() {
    srand(time(0));

    Cartao meuCartao;
    gerarCartao(meuCartao);
    mostrarCartao(meuCartao);

    bool numerosSorteados[MAX_NUM] = {false};

    while (true) {
        int numSorteado = (rand() % MAX_NUM) + 1;

        if (numerosSorteados[numSorteado - 1]) {
            continue;
        }

        numerosSorteados[numSorteado - 1] = true;
        cout << "Número sorteado: " << numSorteado << endl;

        marcarNumero(meuCartao, numSorteado);
        mostrarCartao(meuCartao);

        if (verificarVitoria(meuCartao)) {
            cout << " BINGO! " << endl;
            break;
        }

        cout << "Pressione Enter para sortear o próximo número...";
        cin.ignore();
    }

    return 0;
}
