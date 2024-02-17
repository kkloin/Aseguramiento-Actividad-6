from datetime import datetime

def validar_reserva(fecha_entrada, fecha_salida, tipo_habitacion, servicios_adicionales):
    # Validar las fechas
    formato_fecha = "%d-%m-%Y"
    fecha_entrada = datetime.strptime(fecha_entrada, formato_fecha)
    fecha_salida = datetime.strptime(fecha_salida, formato_fecha)
    if fecha_salida <= fecha_entrada:
        return False

    # Validar el tipo de habitación
    tipos_habitacion_validos = ["individual", "doble", "suite"]
    if tipo_habitacion not in tipos_habitacion_validos:
        return False

    # Validar los servicios adicionales
    servicios_validos = ["wifi", "desayuno", "parking"]
    for servicio in servicios_adicionales:
        if servicio not in servicios_validos:
            return False

    return True
