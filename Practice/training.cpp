#include <iostream>
using namespace std;


int main(){
 int num1;
 cout << "Digite o numero pelo queal sera multiplicado: ";
 cin >> num1;
 int resultado;
for(int i = 1; i<=10; i++){
    resultado = num1 * i;
    cout << num1 << '*' << i << '=' << resultado <<  endl;
}
}