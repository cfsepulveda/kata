from unittest import TestCase
from Numero import Numero

class NumeroTest(TestCase):

    def test_procesarCadena(self):
        self.assertEqual(Numero().resolver(""), [0], "Cadena vacía")
