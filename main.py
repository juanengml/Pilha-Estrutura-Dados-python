from random import randint
import random

from EstruturaDados import Pilha, Filas,ListaEncadeadaSimples

from Arvore import NodoArvore, insere, busca, Organiza

keys = [
{1: ["bola", "arq1.txt"]},
{2: ["casa", "arq1.txt"]},
{2: ["casa", "arq2.txt"]},
{1: ["bola", "arq1.txt"]},
{3: ["dado", "arq3.txt"]},
{3: ["dado", "arq2.txt"]},
{1: ["bola", "arq2.txt"]},
{4: ["arvore", "arq2.txt"]},
{4: ["arvore", "arq1.txt"]}]

### ATP Estrutura Parte 2 

def main():
  
  # inserindo valores na arvore
  raiz = NodoArvore(0)
  for chave in keys:
    key = min(chave.keys())
    print(key,chave[key])
    nodo = NodoArvore(chave=key,lista=chave[key])
    insere(raiz, nodo)
    

  # Procura por valores na árvore.
  ordenar = []
  for chave in keys:
    key = min(chave.keys())
    resultado = busca(raiz, key)
    if resultado:
        print("Busca pela chave {}  Sucesso!".format(chave))
        ordenar.append(chave)
        
    else:
        print("Busca pela chave {} : Falha!".format(chave))  
  
  for arvore in Organiza(ordenar):
    print(arvore)
        


if __name__ == '__main__':
    main()

