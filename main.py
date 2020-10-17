import random
from EstruturaDados import Pilha, Filas

def main():
    pilha = Pilha()

    [pilha.push(random.randint(10,99)) for _ in range(0, 10)]   

    pilha.show()

    [pilha.pop() for _ in range(4)]
    

    pilha.show()

    fila = Filas()

    [fila.insere(random.randint(10, 120)) for _ in range(0, 10)]
        

    fila.show()
    fila.remove()
    fila.remove()
    fila.show()


if __name__ == '__main__':
    main()

if __name__ == "__main__":
    main()