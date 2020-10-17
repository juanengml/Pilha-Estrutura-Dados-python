import random
from EstruturaDados import Pilha

def main():
    pilha = Pilha()

    [pilha.push(random.randint(10,99)) for _ in range(0, 10)]   

    pilha.show()

    [pilha.pop() for _ in range(4)]
    

    pilha.show()


if __name__ == "__main__":
    main()