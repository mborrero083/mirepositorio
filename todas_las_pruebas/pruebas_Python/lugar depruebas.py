"""l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
for m in range((len(l1)-len(l2)),len(l1)-1):
    l2.append(0)
    
print(l2)
print(l1)"""
class nodo:
    def __init__(self,valor):
        self.valor=valor
        self.Next=None
    def __str__(self):
        return str(self.valor)
class listaenlazada:
    def __init__(self):
        self.primero=None
        self.tamanolsita=0

    def agregar(self,valor):
        elnode=nodo(valor)
        if self.tamanolsita==0:
            self.primero=elnode
        else:
            indice=self.primero
            while indice.Next!=None:
                indice=indice.Next
            indice.Next=elnode
        self.tamanolsita+=1
        return elnode

    def __len__(self):
        return self.tamanolsita
    def __str__(self):
        mostrar="["
        indice=self.primero
        while indice!=None:
            mostrar+=str(indice)
            mostrar+=str(",")
            indice=indice.Next
        mostrar+="]"
        return mostrar

milista=listaenlazada()
milista.agregar(1)
milista.agregar(2)
milista.agregar(3)
milista.agregar(4)
print(milista)
print(7%10)