from EstruturaDados import ListaEncadeadaSimples
from collections import Counter
from collections import defaultdict
import itertools

dd = defaultdict(list)


class NodoArvore:
    def __init__(self, chave=None,lista=None, esquerda=None, direita=None):
        self.chave = chave
        self.lista = lista
        self.listaencadeada = ListaEncadeadaSimples()
        self.listaencadeada.append(chave,lista)
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s %s  -> %s' % (
          self.esquerda and self.esquerda.chave,
          self.chave,self.lista,self.direita and  
          self.direita.chave)


def busca(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        #raiz.direita.listaencadeada.show()
        return busca(raiz.direita, chave)
    else:
    # A chave procurada é menor que a da raiz.
        #raiz.esquerda.listaencadeada.show()
        return busca(raiz.esquerda, chave)




def insere(raiz, nodo):
      """Insere um nodo em uma árvore binária de pesquisa."""
      # Nodo deve ser inserido na raiz.
      if raiz is None:
          raiz = nodo

      # Nodo deve ser inserido na subárvore direita.
      elif raiz.chave < nodo.chave:
          if raiz.direita is None:
              raiz.direita = nodo
          else:
              #self.listaencadeada.append(raiz.direita,nodo)
              insere(raiz.direita, nodo)

      # Nodo deve ser inserido na subárvore esquerda.
      else:
          if raiz.esquerda is None:
              raiz.esquerda = nodo
          else:
              insere(raiz.esquerda, nodo)
              #self.listaencadeada.append(raiz.esquerda,nodo)


def Organiza(my_list): 
      
    # Creating an empty dictionary  
    for d in my_list:
       for key, value in d.items():
            dd[key].append(value)
    final_list = []        
    for p in dd:
      freq = [dd[p].count(w) for w in dd[p]]
      new_list = list(num for num,_ in itertools.groupby([{p[0][0]:p[0][1]} for p in list(num for num,_ in itertools.groupby(list(zip(dd[p]))))]))  

      for add in range(len(new_list)):
       try: 
        if new_list[add].keys() == new_list[add+1].keys():
              final_list.append({list(new_list[add])[0]: [list(new_list[add].values())[0], list(new_list[add+1].values())[0] ]})
              
       except IndexError:
         pass
    return final_list