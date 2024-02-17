import re

def validar_registro(email, password):
    # Validar el email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Validar el password
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):  # Debe contener al menos un numero
        return False
    if not re.search(r"[A-Z]", password):  # Debe contener al menos una letra mayuscula
        return False
    if not re.search(r"[a-z]", password):  # Debe contener al menos una letra minuscula
        return False

    return True
