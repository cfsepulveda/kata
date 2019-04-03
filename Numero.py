class Numero:


    def resolver(self, cadena):
        cadena = cadena.replace(' ', '')
        arrNumber = cadena.split(",")
        if not cadena:
            return [0] 
        else:
            return [len(arrNumber)]         


    def resolverDos(self, cadena):
        cadena = cadena.replace(' ', '')
        arrNumber = cadena.split(",")
        if not cadena:
            return [0, 0] 
        else:
            return [len(arrNumber), float(min(arrNumber))]     

    def resolverTres(self, cadena):
        cadena = cadena.replace(' ', '')
        arrNumber = cadena.split(",")
        if not cadena:
            return [0, 0, 0] 
        else:
            return [len(arrNumber), float(min(arrNumber)),  float(max(arrNumber))]     

    def resolverCuatro(self, cadena):
        cadena = cadena.replace(' ', '')
        arrNumber = cadena.split(",")
        if not cadena:
            return [0, 0, 0, 0] 
        else:
            sum=0.0
            for i in range(0,len(arrNumber)):
                sum=sum+float(arrNumber[i])
                promedio = sum/len(arrNumber)
            return [len(arrNumber), float(min(arrNumber)),  float(max(arrNumber)), float(promedio)]     

    