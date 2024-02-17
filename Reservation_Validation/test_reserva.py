import unittest
from reserva import validar_reserva

class TestValidarReserva(unittest.TestCase):
    def test_validar_reserva(self):
        self.assertTrue(validar_reserva("01-01-2024", "02-01-2024", "doble", ["wifi", "desayuno"]))
        self.assertFalse(validar_reserva("02-01-2024", "01-01-2024", "doble", ["wifi", "desayuno"]))
        self.assertFalse(validar_reserva("01-01-2024", "02-01-2024", "triple", ["wifi", "desayuno"]))
        self.assertFalse(validar_reserva("01-01-2024", "02-01-2024", "doble", ["wifi", "piscina"]))

if __name__ == '__main__':
    unittest.main()
