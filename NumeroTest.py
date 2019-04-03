from unittest import TestCase
from Numero import Numero

class NumeroTest(TestCase):

    def test_procesarCadena(self):
        self.assertEqual(Numero().resolver(""), [0], "Cadena vacía")

    def test_procesar_cadena_un_numero_cadena(self):
        self.assertEqual(Numero().resolver("1"), [1], "Un número") 
    
    def test_procesar_cadena_un_dos_cadena(self):
        self.assertEqual(Numero().resolver("1, 2"), [2], "dos números") 