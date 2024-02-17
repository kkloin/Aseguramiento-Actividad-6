import unittest
from registro import validar_registro

class TestValidarRegistro(unittest.TestCase):
    def test_validar_registro(self):
        self.assertTrue(validar_registro("Usuario@Ejemplo.com", "Contrasena1"))
        self.assertFalse(validar_registro("usuarioejemplo.com", "Contrasena1"))
        self.assertFalse(validar_registro("Usuario@Ejemplo.com", "corta"))
        self.assertFalse(validar_registro("Usuario@Ejemplo.com", "SINMINUSCULA1"))
        self.assertFalse(validar_registro("Usuario@Ejemplo.com", "sinnumero"))

if __name__ == '__main__':
    unittest.main()
