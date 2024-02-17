# reserva.py

Se definne la función _validar_registro_ que toma un correo electrónico y una contraseña como entrada y devuelve **True** si el correo electrónico y la contraseña son válidos, y **False** en caso contrario. Para este caso, vamos a considerar un correo electrónico válido si contiene un “@” y un “.”, y una contraseña válida si tiene al menos 12 caracteres. Además de esto, también se comprueba que la contraseña tenga al menos 8 caracteres, al menos un número, al menos una letra mayúscula y al menos una letra minúscula.

# test_reserva.py

En este código de prueba, estamos importando el módulo _unittest_ y definiendo una clase _TestValidarRegistro_ que hereda de _unittest.TestCase_. Dentro de esta clase, definimos un método _test_validar_registro_ que contiene nuestras afirmaciones de prueba. Estas afirmaciones comprueban que la función **validar_registro** devuelve el resultado esperado para varios pares de entradas.
