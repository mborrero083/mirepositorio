class Solution(object):
    def longestPalindrome(self, s):
            ya_estan=[]
            indices_palindromos=[]
            palabra_palindroma=[]
            for i in s:
                if i not in ya_estan and s.count(i)>1 :
                    ya_estan.append(i)
                    indices=self.indices_de_la_letra(i,s,indices_palindromos)
                    if indices!=False and len(indices)>1: 
                        el_palindromo=self.palindromo(indices,s,indices_palindromos)
                        if el_palindromo!=[]:
                            palabra_palindroma.append(el_palindromo)
            if palabra_palindroma!=[]:
                return(max(palabra_palindroma,key=len))
            else:
                return(s[0])
        
    def indices_de_la_letra(self,letra,cadena,indices_palindromos):
        indices=[]
        indice=0
        if indices_palindromos!=[] :
            maximo=max(indices_palindromos)
            minimo=min(indices_palindromos)
            while cadena.find(letra,indice)!=-1:
                indice=cadena.find(letra,indice)
                if minimo<indice<maximo:
                    indice+=1
                else:
                    indices.append(indice)
                    indice+=1
        else:
            while cadena.find(letra,indice)!=-1:
                indice=cadena.find(letra,indice)
                indices.append(indice)
                indice+=1
        return(indices)

    def palindromo(self,indices,cadena,indices_palindromos):
        palabras=""
        palabras=[]
        izquierda=0
        derecha=len(indices)-1
        while izquierda<derecha:
            if cadena[indices[izquierda]]==cadena[indices[derecha]] and cadena[indices[izquierda]+1]==cadena[indices[derecha]-1]:
                palabra=cadena[indices[izquierda]:indices[derecha]+1]
                inver_plabra=palabra[::-1]
                if palabra==inver_plabra and palabra!=palabras and len(palabra)>len(palabras):
                    palabras=palabra
                    indices_palindromos=[]
                    indices_palindromos.append(indices[izquierda])
                    indices_palindromos.append(indices[derecha])
                    derecha-=1
                    izquierda=0
                else:
                    izquierda+=1
            else:
                izquierda+=1
            if izquierda==derecha:
                izquierda=0
                derecha-=1
        return(palabras)

Solution().longestPalindrome("abacab")