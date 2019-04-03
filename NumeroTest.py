from unittest import TestCase
from Numero import Numero

class NumeroTest(TestCase):

    def test_procesarCadena(self):
        self.assertEqual(Numero().resolver(""), [], "Cadena vacía")

    def test_procesar_cadena_un_numero_cadena(self):
        self.assertEqual(Numero().resolver("1"), [1], "Un número") 