#class busquedaengoogle:
#    def __init__(self,que_buscar):
#        self.que_buscar=que_buscar
#
#   def hacer_busqueda_google(self):
#        print("Busque",self.que_buscar)
#
#    def concatenar_con_otra_palabra(self,otra_busqueda):
#        self.otra_busqueda=otra_busqueda
#        print(self.que_buscar+" "+self.otra_busqueda) 
class Solution(object):
    def longestPalindrome(self, s):
        indices=self.indices_letra(s)
        indices_alreves=indices[::-1]
        if indices!=[]:
            for i in indices:
                for m in indices_alreves:
                    if i<m:
                        palindromo=s[i:m+1]
                        palindoromo_reves=palindromo[::-1]
                        if palindromo==palindoromo_reves:
                            return(palindromo)
                    else:
                        pass
        else:
            print(s[0])

    def indices_letra(self,palabra):
        indices=[]
        indice=0
        for letra in palabra:
            if palabra.count(letra)>1:
                indice=palabra.index(letra,indice)
                indices.append(indice)
                indice=indice+1
        return(indices)

print (Solution().longestPalindrome("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu"))

#"cbbd"
#"abb"
#"ac"
#"babad"