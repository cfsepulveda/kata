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
            return [len(arrNumber), float(min(arrNumber)), 0]     