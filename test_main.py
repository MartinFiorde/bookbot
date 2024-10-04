import os
import unittest
from main import count_words

# CLI command to execute tests: python3 -m unittest test_main.py

class Test_count_words(unittest.TestCase):

    def test_contar_palabras(self):
        # Prepara un archivo de prueba
        path = 'test_archivo.txt'
        with open(path, 'w', encoding='utf-8') as f:
            f.write("Hola mundo\nEste es un test.\nContemos las palabras.")

        # Prueba la función contar_palabras
        resultado = count_words(path)
        self.assertEqual(resultado, 9)  # Debe contar 9 palabras

        os.remove(path)

    def test_archivo_vacio(self):
        # Prepara un archivo vacío
        path = 'archivo_vacio.txt'
        with open(path, 'w', encoding='utf-8') as f:
            pass  # Crear un archivo vacío

        resultado = count_words(path)
        self.assertEqual(resultado, 0)  # Debe contar 0 palabras

        os.remove(path)

    def test_archivo_no_encontrado(self):
        resultado = count_words('archivo_inexistente.txt')
        self.assertEqual(resultado, 0)  # Debe manejar archivos no encontrados

if __name__ == '__main__':
    unittest.main()
