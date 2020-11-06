from random import randint
import random

from EstruturaDados import Pilha, Filas,ListaEncadeadaSimples
from Arvore import NodoArvore, insere, busca, Organiza, BuscadorATP3 


keys = [
{1: ["bola", "arq1.txt"]},
{2: ["casa", "arq1.txt"]},
{2: ["casa", "arq2.txt"]},
{1: ["bola", "arq1.txt"]},
{3: ["dado", "arq1.txt"]},
{3: ["dado", "arq1.txt"]},
{3: ["dado", "arq2.txt"]},
{3: ["dado", "arq3.txt"]},
{3: ["dado", "arq2.txt"]},
{4: ["arvore", "arq1.txt"]},
{4: ["arvore", "arq2.txt"]}]


# ATP 3 



def main():
  
  # inserindo valores na arvore ATP 2 
  raiz = NodoArvore(0)
  for chave in keys:
    key = min(chave.keys())
    #print(key,chave[key])
    nodo = NodoArvore(chave=key,lista=chave[key])
    insere(raiz, nodo)
    

  # Procura por( valores na árvore.
  
  
  menu = str(input("Entre com os termos a ser pesquisados (separados por espaço): "))
  #menu = "dado"
  for termo in menu.split():
    print("-"*20, termo, "-"*20)
    result = BuscadorATP3(raiz, keys, termo)
    print("Resultado da busca - ",result['processado'])
    
        


if __name__ == '__main__':
    main()

