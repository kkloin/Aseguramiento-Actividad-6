# reserva.py

Se define la función _validar_reserva_ que toma las fechas de entrada y salida, el tipo de habitación y los servicios adicionales como entrada y devuelve **True** si todos los datos son válidos, y **False** en caso contrario. Para este ejemplo, vamos a considerar que las fechas son válidas si la fecha de salida es posterior a la fecha de entrada, el tipo de habitación es válido si es una de las opciones predefinidas, y los servicios adicionales son válidos si son una lista de opciones predefinidas.

# test_reserva.py

En este caso, se importan el módulo _unittest_ y se define una clase _TestValidarReserva_ que hereda de _unittest.TestCase_. Dentro de esta clase, se define un método **test_validar_reserva** que contiene las afirmaciones de prueba. Estas afirmaciones comprueban que la función _validar_reserva_ devuelve el resultado esperado para varios conjuntos de entradas.
