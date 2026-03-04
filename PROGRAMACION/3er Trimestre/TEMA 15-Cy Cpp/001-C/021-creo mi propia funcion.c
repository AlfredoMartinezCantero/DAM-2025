#include <stdio.h>

int calculoDoble(int numero){
	int doble = numero*2;
  return doble;
}

int main(){
    int edad = 24;
    int midoble = calculoDoble(edad);
    printf("El doble es: %i",midoble);
    return 0;
}