from unittest import TestCase
from Numero import Numero

class NumeroTest(TestCase):

    #Iteración 1

    def test_procesarCadena(self):
        self.assertEqual(Numero().resolver(""), [0], "Cadena vacía")

    def test_procesar_cadena_un_numero_cadena(self):
        self.assertEqual(Numero().resolver("1"), [1], "Un número") 
    
    def test_procesar_cadena_dos_cadena(self):
        self.assertEqual(Numero().resolver("1, 2"), [2], "dos números") 
        
    def test_procesar_cadena_seis_cadena(self):
        self.assertEqual(Numero().resolver("1, 2, 4, 5, 5, 4"), [6], "6 números")         

        #Iteración 2

    def test_procesarCadena_dos(self):
        self.assertEqual(Numero().resolverDos(""), [0, 0], "Cadena vacía")

    def test_procesar_cadena_un_numeros_cadena_dos(self):
        self.assertEqual(Numero().resolverDos("1"), [1, 1], "Un número") 

    def test_procesar_cadena_dos_numeros_cadena_dos(self):
        self.assertEqual(Numero().resolverDos("1, 2"), [2, 1], "dos números") 

    def test_procesar_cadena_n_numeros_cadena_dos(self):
        self.assertEqual(Numero().resolverDos("1, 2, 0 ,4"), [4, 0], "n números") 


        #Iteración 3
    def test_procesarCadena_tres(self):
        self.assertEqual(Numero().resolverTres(""), [0, 0, 0], "Cadena vacía")

    def test_procesar_cadena_un_numeros_cadena_tres(self):
        self.assertEqual(Numero().resolverTres("1"), [1, 1, 1], "Un numero")

    def test_procesar_cadena_dos_numeros_cadena_tres(self):
        self.assertEqual(Numero().resolverTres("1, 4"), [2, 1, 4], "dos numero")

    def test_procesar_cadena_cinco_numeros_cadena_tres(self):
        self.assertEqual(Numero().resolverTres("1, 4, 4 ,3, 4"), [5, 1, 4], "5 numero")


        #Iteración 4
    def test_procesarCadena_cuatro(self):
        self.assertEqual(Numero().resolverCuatro(""), [0, 0, 0, 0], "Cadena vacía")

    def test_procesar_cadena_un_numeros_cadena_cuatro(self):
        self.assertEqual(Numero().resolverCuatro("1"), [1, 1, 1, 1], "Cadena vacía")

    def test_procesar_cadena_dos_numeros_cadena_cuatro(self):
        self.assertEqual(Numero().resolverCuatro("1, 9"), [1, 1, 9, 5], "Cadena vacía")        