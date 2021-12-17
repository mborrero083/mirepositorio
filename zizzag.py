def convert(s, numRows):
    palabra=""
    organizado={}
    controlador=numRows-1
    validar=True
    for numero in range(len(s)):
        if numero<numRows:
            organizado[numero]=[]
            organizado[numero].append(s[numero])
        elif  controlador==numRows-1 and  validar==True:
            if numRows-1!=0:
                controlador=controlador-1
                organizado[controlador].append(s[numero])
                controlador=controlador-1
            else:
                organizado[controlador].append(s[numero])
        elif  0<=controlador<numRows-1 and validar==True:
            organizado[controlador].append(s[numero])
            controlador=controlador-1
        elif  controlador<0 and  validar==True:
            validar=False
            controlador=controlador+2
            organizado[controlador].append(s[numero])
        elif  controlador<numRows-1 and  validar==False:
            controlador=controlador+1
            organizado[controlador].append(s[numero])
        elif controlador>=numRows-1 and  validar==False:
            validar=True
            controlador=controlador-1
            organizado[controlador].append(s[numero])
            controlador=controlador-1
    for (k,v) in organizado.items():
        palabra=palabra+"".join(v)
    print(palabra)
    


s="ABC"
convert(s,1)
#"PAYPALISHIRING"