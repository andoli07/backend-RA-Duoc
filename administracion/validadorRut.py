import re
from django.core.exceptions import ValidationError

def validar_rut(rut):
    """
    Valida un RUT chileno, tanto el formato como el dígito verificador.
    """
    # 1. Eliminar espacios y convertir a mayúsculas
    rut = rut.strip().upper()

    # 2. Verificar que el RUT tenga el formato adecuado
    if not re.match(r'^\d{7,8}-[\dK]$', rut):
        return False  # Formato incorrecto

    # 3. Separar el RUT del dígito verificador
    rut_base, dv = rut.split('-')

    # 4. Calcular el dígito verificador
    return rut_valido(rut_base, dv)

def rut_valido(rut_base, dv):
    """
    Calcula y valida el dígito verificador del RUT chileno.
    """
    rut_base = list(map(int, rut_base[::-1]))  # Invertimos el RUT y lo convertimos en lista de enteros
    multiplicadores = [2, 3, 4, 5, 6, 7] * ((len(rut_base) // 6) + 1)
    suma = sum([a * b for a, b in zip(rut_base, multiplicadores)])

    resto = suma % 11
    dv_calculado = 11 - resto
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)

    return dv == dv_calculado

# Este es el validador que usaremos en el modelo
def validador_rut_django(valor):
    if not validar_rut(valor):
        raise ValidationError("El RUT ingresado no es válido.")