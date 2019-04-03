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
        self.assertEqual(Numero().resolver(""), [0, 0], "Cadena vacía")