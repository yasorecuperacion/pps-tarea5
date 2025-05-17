import unittest

# Importa función esPalindromo
from charfun import esPalindromo

class TestCharfun(unittest.TestCase):

    def test_palindromos_parametrizados(self):
        # Lista de pruebas parametrizadas: (cadena, resultado mensaje)
        lista_de_pruebas = [
            ("Anita lava la tinaa", True, "Se espera una cadena que es un palíndromo con espacios y mayúsculas"),
            ("Anita lava la tinaa", False, "Se espera una cadena que no es un palíndromo"),
            ("Re  Co  no ceR", True, "Se espera una cadena palíndromo con espacios adicionales"),
            ("", True, "Se espera una cadena vacía"),
            ("a", True, "Se espera una cadena con una sola letra"),
            ("!a!", True, "Se espera una cadena con caracteres especiales"),
        ]

        # Recorre la lista sobre los casos y realizar subtests
        for cadena, resultado, mensaje in lista_de_pruebas:
            # Crea un subtest para poder lanzar todos las pruebas y cuando una falle el programa no falle
            # al final muestra el resultado en el caso de que haya fallado alguna
            with self.subTest(cadena=cadena):
                self.assertEqual(esPalindromo(cadena), resultado, mensaje)

if __name__ == '__main__':
    unittest.main()
